package org.reyrun.mobiletest;
import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceError;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;
import org.json.JSONArray;
import org.json.JSONObject;

public final class ProbeActivity extends Activity {
    private WebView page;
    private JSONArray pages;
    private final JSONArray results = new JSONArray();
    private String script;
    private int polls;
    private String asset(String name) throws Exception {
        try(InputStream f=getAssets().open(name);ByteArrayOutputStream out=new ByteArrayOutputStream()){
            byte[] buffer=new byte[4096];int count;
            while((count=f.read(buffer))!=-1) out.write(buffer,0,count);
            return out.toString("UTF-8");
        }
    }
    public void onCreate(Bundle saved){
        super.onCreate(saved);
        try{
            pages=new JSONArray(asset("pages.json"));script=asset("geometry.js");
            page=new WebView(this);setContentView(page);
            page.getSettings().setJavaScriptEnabled(true);
            page.getSettings().setDomStorageEnabled(true);
            page.getSettings().setUseWideViewPort(true);
            page.getSettings().setLoadWithOverviewMode(true);
            page.setWebViewClient(new WebViewClient(){
                @Override public void onPageFinished(WebView web,String url){page.postDelayed(ProbeActivity.this::inspect,300);}
                @Override public void onReceivedError(WebView web,WebResourceRequest req,WebResourceError err){
                    if(req.isForMainFrame()) Log.e("ReyrunMobile","ERROR "+req.getUrl()+" "+err.getDescription());
                }
            });
            next();
        }catch(Exception e){Log.e("ReyrunMobile","ERROR "+e);}
    }
    private void next() throws Exception {
        polls=0;page.loadUrl(pages.getJSONArray(results.length()).getString(0));
    }
    private void inspect(){
        page.evaluateJavascript(script,s->{
            try{
                JSONObject row=new JSONObject(s);
                if(row.getJSONArray("image").getInt(0)==0 && ++polls<60){page.postDelayed(this::inspect,250);return;}
                Log.i("ReyrunMobile","ROW "+row);
                results.put(row);
                if(results.length()<pages.length())next();
                else Log.i("ReyrunMobile","DONE "+WebView.getCurrentWebViewPackage().versionName);
            }catch(Exception e){Log.e("ReyrunMobile","ERROR "+e);}
        });
    }
}
