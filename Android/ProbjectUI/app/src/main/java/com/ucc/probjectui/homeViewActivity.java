package com.ucc.probjectui;

import android.bluetooth.BluetoothAdapter;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Locale;

public class homeViewActivity extends AppCompatActivity {

    private static final String TAG = "main";
    private Context context;
    private ImageView imageViewRoom1, imageViewRoom2, imageViewRoom3;
    private TextView resultData;
    private getMessage resultMessage;
    private StringBuilder webUrl;
    private String httpurl = "http://";
    private String selectData = ":5000/test1";
    private EditText editIP;
    private URL url;
    private Button buttonOK;
    private TextView textViewTemp, textViewHum;
    private String ipAddr;
    private int actionFlag = 1;
    private String ledData = ":5000/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_view);

        context = this;
        setTitle("WEB View");

        imageViewRoom1 = (ImageView) findViewById(R.id.imageView_room1);
        imageViewRoom2 = (ImageView) findViewById(R.id.imageView_room2);
        imageViewRoom3 = (ImageView) findViewById(R.id.imageView_room3);

        resultData = (TextView) findViewById(R.id.textView_resultData);
        resultData.setText("");

        imageViewRoom1.setOnClickListener(new viewtempClick());
        imageViewRoom2.setOnClickListener(new viewtempClick());
        imageViewRoom3.setOnClickListener(new viewtempClick());

        textViewTemp = (TextView) findViewById(R.id.textView_temp);
        //textViewHum = (TextView) findViewById(R.id.textView_hum);
        textViewTemp.setText("");
        //textViewHum.setText("");

        textViewTemp.setOnClickListener(new viewClick());
        //textViewHum.setOnClickListener(new viewClick());

        editIP = (EditText) findViewById(R.id.editText_viewIP);

        buttonOK = (Button) findViewById(R.id.button_viewLink);

        buttonOK.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                resultMessage = new getMessage();
                resultMessage.execute();

            }
        });

    }

    private class viewClick implements View.OnClickListener {
        @Override
        public void onClick(View v) {

            resultMessage = new getMessage();
            resultMessage.execute();

        }


    }

    private class viewtempClick implements View.OnClickListener {
        @Override
        public void onClick(View v) {

             resultMessage = new getMessage();
             resultMessage.execute();
        }
    }

    private class getMessage extends AsyncTask<Void, Void, String> {
        @Override
        protected String doInBackground(Void... voids) {
            String data = null;

            ipAddr = editIP.getText().toString();

            webUrl = new StringBuilder();
            webUrl.append(httpurl);
            webUrl.append(ipAddr);
            webUrl.append(selectData);
            Log.d(TAG, "webaddr= "+webUrl);

            try{

                url = new URL(webUrl.toString());
                Log.d(TAG,"url = "+url);

                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");

                int code =  conn.getResponseCode();
                Log.d(TAG, "code = "+code);

                InputStream input = conn.getInputStream();
                InputStreamReader reader = new InputStreamReader(input, "utf-8");

                char[] buffer = new char[50];
                reader.read(buffer);

                data = String.valueOf(buffer);

                input.close();

            }catch (MalformedURLException e){
                e.printStackTrace();
            }catch (IOException e){
                e.printStackTrace();
            }

            return data;
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            String messageData;
            resultData.setText(s);

            String getText = resultData.getText().toString();

                messageData = getText.substring(18, 22);
                textViewTemp.setText(messageData);
                resultData.setText("");
                Log.d(TAG, "result = "+messageData);


        }
    }


}
