#import <TargetConditionals.h>
#import <WebKit/WebKit.h>
#if TARGET_OS_OSX
#import <AppKit/AppKit.h>
#else
#import <UIKit/UIKit.h>
#endif

@interface Survey : NSObject <WKNavigationDelegate>
@property(strong) WKWebView *view;
@property(strong) NSArray *pages;
@property(strong) NSMutableArray *rows;
@property(copy) NSString *script;
@property(copy) NSString *destination;
@property NSInteger attempts;
@property BOOL inspecting;
- (void)start;
@end
@implementation Survey
- (void)write:(NSDictionary *)data {
    [[NSJSONSerialization dataWithJSONObject:data options:0 error:nil] writeToFile:self.destination atomically:YES];
#if TARGET_OS_OSX
    [NSApp terminate:nil];
#endif
}
- (void)loadNext {
    self.attempts=0; self.inspecting=NO;
    NSString *url=self.pages[self.rows.count][0];
    [self.view loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:url]]];
}
- (void)start {
    self.rows=[NSMutableArray array];
    self.view.navigationDelegate=self;
    [self loadNext];
}
- (void)inspect {
    [self.view evaluateJavaScript:self.script completionHandler:^(id value, NSError *error){
        if(error || ![value isKindOfClass:NSDictionary.class]){
            [self write:@{@"error":error.localizedDescription ?: @"Page produced no measurements"}]; return;
        }
        NSDictionary *row=value;
        if([row[@"image"][0] integerValue]==0 && ++self.attempts<60){
            dispatch_after(dispatch_time(DISPATCH_TIME_NOW,250*NSEC_PER_MSEC),dispatch_get_main_queue(),^{[self inspect];}); return;
        }
        [self.rows addObject:row];
        if(self.rows.count==self.pages.count) [self write:@{@"pages":self.rows}];
        else [self loadNext];
    }];
}
- (void)webView:(WKWebView *)view didFinishNavigation:(WKNavigation *)nav {
    if(self.inspecting) return;
    self.inspecting=YES;
    [self inspect];
}
- (void)webView:(WKWebView *)view didFailProvisionalNavigation:(WKNavigation *)nav withError:(NSError *)error {
    if(error.code!=NSURLErrorCancelled) [self write:@{@"error":error.localizedDescription,@"url":self.pages[self.rows.count][0]}];
}
@end

static Survey *survey;
static void setup(WKWebView *view, NSString *dir, NSString *out) {
    survey=[Survey new]; survey.view=view; survey.destination=out;
    survey.pages=[NSJSONSerialization JSONObjectWithData:[NSData dataWithContentsOfFile:[dir stringByAppendingPathComponent:@"pages.json"]] options:0 error:nil];
    survey.script=[NSString stringWithContentsOfFile:[dir stringByAppendingPathComponent:@"geometry.js"] encoding:NSUTF8StringEncoding error:nil];
    [survey start];
}
#if TARGET_OS_OSX
int main(int argc,char **argv){
    @autoreleasepool{
        [NSApplication sharedApplication];
        [NSApp setActivationPolicy:NSApplicationActivationPolicyAccessory];
        NSRect frame=NSMakeRect(0,0,1440,900);
        NSWindow *window=[[NSWindow alloc] initWithContentRect:frame styleMask:NSWindowStyleMaskBorderless backing:NSBackingStoreBuffered defer:NO];
        WKWebView *web=[[WKWebView alloc] initWithFrame:frame configuration:[WKWebViewConfiguration new]];
        window.contentView=web; [window orderFront:nil];
        setup(web,[NSString stringWithUTF8String:argv[1]],[NSString stringWithUTF8String:argv[2]]);
        [NSApp run];
        (void)window;
    }return 0;
}
#else
@interface Scene : UIResponder <UIWindowSceneDelegate>
@property(strong) UIWindow *window;
@end
@implementation Scene
- (void)scene:(UIScene *)scene willConnectToSession:(UISceneSession *)session options:(UISceneConnectionOptions *)options {
    self.window=[[UIWindow alloc] initWithWindowScene:(UIWindowScene *)scene];
    UIViewController *controller=[UIViewController new];
    WKWebView *web=[[WKWebView alloc] initWithFrame:self.window.bounds configuration:[WKWebViewConfiguration new]];
    controller.view=web;self.window.rootViewController=controller;[self.window makeKeyAndVisible];
    NSString *documents=[[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask].firstObject.path;
    setup(web,NSBundle.mainBundle.resourcePath,[documents stringByAppendingPathComponent:@"smoke-result.json"]);
}
@end
@interface App : UIResponder <UIApplicationDelegate>
@end
@implementation App
- (UISceneConfiguration *)application:(UIApplication *)a configurationForConnectingSceneSession:(UISceneSession *)s options:(UISceneConnectionOptions *)o{
    UISceneConfiguration *cfg=[[UISceneConfiguration alloc] initWithName:@"Smoke" sessionRole:s.role];cfg.delegateClass=Scene.class;return cfg;
}
@end
int main(int argc,char **argv){@autoreleasepool{return UIApplicationMain(argc,argv,nil,NSStringFromClass(App.class));}}
#endif
