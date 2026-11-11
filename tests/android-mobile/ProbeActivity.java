package org.reyrun.mobiletest;

import android.app.Activity;
import android.content.pm.PackageInfo;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import org.json.JSONArray;
import org.json.JSONObject;

public final class ProbeActivity extends Activity {
    private static final String TAG = "ReyrunMobile";
    private WebView page;
    private boolean announced;

    @Override public void onCreate(Bundle state) {
        super.onCreate(state);
        page = new WebView(this);
        setContentView(page);
        page.getSettings().setJavaScriptEnabled(true);
        page.getSettings().setUseWideViewPort(true);
        page.getSettings().setLoadWithOverviewMode(true);
        page.setWebViewClient(new WebViewClient() {
            @Override public void onPageFinished(WebView view, String url) {
                page.postDelayed(ProbeActivity.this::inspect, 250);
            }
        });
        try (InputStream file = getAssets().open("index.html")) {
            ByteArrayOutputStream content = new ByteArrayOutputStream();
            byte[] buffer = new byte[4096];
            int count;
            while ((count = file.read(buffer)) != -1) content.write(buffer, 0, count);
            page.loadDataWithBaseURL("https://appassets.androidplatform.net/",
                new String(content.toByteArray(), StandardCharsets.UTF_8), "text/html", "UTF-8", null);
        } catch (Exception error) {
            Log.e(TAG, "ERROR " + error);
        }
    }

    private void inspect() {
        // Read geometry and result only. The host driver taps through Android's input service.
        String inspect = "(function(){const b=document.getElementById('demo');if(!b)return null;"
            + "const r=b.getBoundingClientRect();const out=document.getElementById('output');"
            + "return [innerWidth,r.left+r.width/2,r.top+r.height/2,"
            + "out.hidden?'':document.getElementById('result').value,window.isSecureContext];})()";
        page.evaluateJavascript(inspect, result -> {
            try {
                if (!"null".equals(result)) {
                    JSONArray data = new JSONArray(result);
                    if (!data.getBoolean(4)) throw new Exception("Insecure renderer context");
                    if (!data.getString(3).isEmpty()) {
                        PackageInfo provider = WebView.getCurrentWebViewPackage();
                        JSONObject evidence = new JSONObject();
                        evidence.put("androidApi", Build.VERSION.SDK_INT);
                        evidence.put("androidRelease", Build.VERSION.RELEASE);
                        evidence.put("webviewPackage", provider.packageName);
                        evidence.put("webviewVersion", provider.versionName);
                        evidence.put("receipt", new JSONObject(data.getString(3)));
                        Log.i(TAG, "RESULT " + evidence);
                        return;
                    }
                    if (!announced && page.getWidth() > 0 && data.getDouble(0) > 0) {
                        int[] origin = new int[2];
                        page.getLocationOnScreen(origin);
                        double scale = page.getWidth() / data.getDouble(0);
                        long x = origin[0] + Math.round(data.getDouble(1) * scale);
                        long y = origin[1] + Math.round(data.getDouble(2) * scale);
                        Log.i(TAG, "BUTTON " + x + " " + y);
                        announced = true;
                    }
                }
                page.postDelayed(this::inspect, 200);
            } catch (Exception error) {
                Log.e(TAG, "ERROR " + error);
            }
        });
    }
}
