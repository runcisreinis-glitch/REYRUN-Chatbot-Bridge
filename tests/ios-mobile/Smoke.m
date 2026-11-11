#import <UIKit/UIKit.h>
#import <WebKit/WebKit.h>

static void saveResult(NSDictionary *result) {
    NSURL *documents = [[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask].firstObject;
    NSData *json = [NSJSONSerialization dataWithJSONObject:result options:0 error:nil];
    [json writeToURL:[documents URLByAppendingPathComponent:@"smoke-result.json"] atomically:YES];
}

@interface Screen : UIViewController <WKNavigationDelegate>
@end

@implementation Screen
- (void)loadView {
    WKWebView *web = [[WKWebView alloc] initWithFrame:CGRectZero configuration:[[WKWebViewConfiguration alloc] init]];
    web.navigationDelegate = self;
    self.view = web;
    NSString *url = [[NSBundle mainBundle] objectForInfoDictionaryKey:@"REYRUNTestURL"];
    [web loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:url]]];
}

- (void)webView:(WKWebView *)web didFinishNavigation:(WKNavigation *)navigation {
    NSURL *url = [[NSBundle mainBundle] URLForResource:@"scenario" withExtension:@"js"];
    NSError *readError = nil;
    NSString *script = [NSString stringWithContentsOfURL:url encoding:NSUTF8StringEncoding error:&readError];
    if (!script) { saveResult(@{@"error":readError.localizedDescription}); return; }
    [web callAsyncJavaScript:script arguments:@{} inFrame:nil inContentWorld:WKContentWorld.pageWorld completionHandler:^(id value, NSError *error) {
        if (error) saveResult(@{@"error":error.localizedDescription, @"details":error.userInfo.description});
        else if ([value isKindOfClass:NSDictionary.class]) saveResult(value);
        else saveResult(@{@"error":@"No receipt returned."});
    }];
}
- (void)webView:(WKWebView *)web didFailProvisionalNavigation:(WKNavigation *)navigation withError:(NSError *)error {
    saveResult(@{@"error":error.localizedDescription});
}
@end

@interface Scene : UIResponder <UIWindowSceneDelegate>
@property (nonatomic, strong) UIWindow *window;
@end
@implementation Scene
- (void)scene:(UIScene *)scene willConnectToSession:(UISceneSession *)session options:(UISceneConnectionOptions *)options {
    self.window = [[UIWindow alloc] initWithWindowScene:(UIWindowScene *)scene];
    self.window.rootViewController = [[Screen alloc] init];
    [self.window makeKeyAndVisible];
}
@end
@interface App : UIResponder <UIApplicationDelegate>
@end
@implementation App
- (UISceneConfiguration *)application:(UIApplication *)app configurationForConnectingSceneSession:(UISceneSession *)session options:(UISceneConnectionOptions *)options {
    UISceneConfiguration *config = [[UISceneConfiguration alloc] initWithName:@"Smoke" sessionRole:session.role];
    config.delegateClass = Scene.class;
    return config;
}
@end

int main(int argc, char **argv) {
    @autoreleasepool { return UIApplicationMain(argc, argv, nil, NSStringFromClass(App.class)); }
}
