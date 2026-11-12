#import <AppKit/AppKit.h>
#import <WebKit/WebKit.h>

@interface PageProbe : NSObject<WKNavigationDelegate>
@property(nonatomic,strong) WKWebView *view;
@property(nonatomic,strong) NSWindow *window;
@property(nonatomic,copy) NSString *requestedURL;
@property(nonatomic,strong) NSMutableArray *responses;
@property(nonatomic) NSInteger navigationCount;
@property(nonatomic) BOOL finished;
@end

@implementation PageProbe
- (void)finish:(NSDictionary *)fields {
    if (self.finished) return;
    self.finished = YES;
    NSMutableDictionary *result = [fields mutableCopy];
    result[@"url"] = self.requestedURL;
    result[@"responses"] = self.responses;
    result[@"finalURL"] = self.view.URL.absoluteString ?: @"";
    NSData *serialized = [NSJSONSerialization dataWithJSONObject:result options:0 error:nil];
    fwrite(serialized.bytes, 1, serialized.length, stdout);
    puts("");
    fflush(stdout);
    [NSApp terminate:nil];
}
- (void)webView:(WKWebView *)webView decidePolicyForNavigationResponse:(WKNavigationResponse *)navigation
 decisionHandler:(void (^)(WKNavigationResponsePolicy))decisionHandler {
    if (navigation.isForMainFrame && [navigation.response isKindOfClass:NSHTTPURLResponse.class]) {
        NSHTTPURLResponse *response = (NSHTTPURLResponse *)navigation.response;
        NSMutableDictionary *headers = [NSMutableDictionary dictionary];
        for (NSString *key in @[@"content-type", @"server", @"cf-mitigated"]) {
            NSString *value = [response valueForHTTPHeaderField:key];
            if (value) headers[key] = value;
        }
        [self.responses addObject:@{@"status": @(response.statusCode), @"url": response.URL.absoluteString, @"headers": headers}];
    }
    decisionHandler(WKNavigationResponsePolicyAllow);
}
- (void)webView:(WKWebView *)webView didStartProvisionalNavigation:(WKNavigation *)navigation {
    self.navigationCount++;
}
- (void)webView:(WKWebView *)webView didFinishNavigation:(WKNavigation *)navigation {
    NSInteger count = self.navigationCount;
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 5 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
        if (self.finished || count != self.navigationCount || webView.isLoading) return;
        NSString *js = @"(() => {const text=document.body?.innerText||'';return {title:document.title,heading:document.querySelector('h1')?.innerText||'',containsBrand:/REYRUN/i.test(text),excerpt:text.slice(0,240),ua:navigator.userAgent}})()";
        [webView evaluateJavaScript:js completionHandler:^(id value, NSError *error){
            if (error) [self finish:@{@"error":error.localizedDescription}];
            else [self finish:@{@"rendered":value}];
        }];
    });
}
- (void)webView:(WKWebView *)webView didFailProvisionalNavigation:(WKNavigation *)navigation withError:(NSError *)error {
    if (error.code != NSURLErrorCancelled) [self finish:@{@"error":error.localizedDescription, @"errorDomain":error.domain, @"code":@(error.code)}];
}
- (void)webView:(WKWebView *)webView didFailNavigation:(WKNavigation *)navigation withError:(NSError *)error {
    if (error.code != NSURLErrorCancelled) [self finish:@{@"error":error.localizedDescription, @"errorDomain":error.domain, @"code":@(error.code)}];
}
- (void)start:(NSString *)url {
    self.requestedURL = url;
    self.responses = [NSMutableArray array];
    NSRect frame = NSMakeRect(0, 0, 1080, 760);
    WKWebViewConfiguration *config = [WKWebViewConfiguration new];
    config.websiteDataStore = [WKWebsiteDataStore nonPersistentDataStore];
    self.view = [[WKWebView alloc] initWithFrame:frame configuration:config];
    self.view.navigationDelegate = self;
    self.window = [[NSWindow alloc] initWithContentRect:frame styleMask:NSWindowStyleMaskTitled backing:NSBackingStoreBuffered defer:NO];
    self.window.contentView = self.view;
    [self.window makeKeyAndOrderFront:nil];
    [self.view loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:url]]];
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 45 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
        [self finish:@{@"error":@"No completed navigation within 45 seconds"}];
    });
}
@end

int main(int argc, const char **argv) {
    @autoreleasepool {
        if (argc != 2) return 2;
        [NSApplication sharedApplication];
        [NSApp setActivationPolicy:NSApplicationActivationPolicyAccessory];
        [NSApp finishLaunching];
        PageProbe *probe = [PageProbe new];
        [probe start:[NSString stringWithUTF8String:argv[1]]];
        [NSApp run];
    }
    return 0;
}
