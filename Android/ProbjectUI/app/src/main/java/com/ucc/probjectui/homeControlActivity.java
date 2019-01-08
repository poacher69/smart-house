package com.ucc.probjectui;

import android.content.Context;
import android.location.LocationManager;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class homeControlActivity extends AppCompatActivity {

    private static final String TAG = "main";
    private Switch room1switch, room2switch, room3switch, fanswitch;
    private boolean room1SW = false, room2SW = false, room3SW = false, fanSW = false;
    private EditText ipAddr;
    private Context context;
    private String ipAddrData;
    private URLData sendURLData;
    private StringBuilder webURL;
    private URL url;

    private String httpUrl = "http://";
    private String webUrl = ":5000/";
    private String ledport;
    private Button ipLink;
    private TextView resultData;
    private Button room1ButtonON, room1ButtonOFF, room2ButtonON, room2ButtonOFF;
    private Button room3ButtonON, room3ButtonOFF, fanButtonON, fanButtonOFF;
    private int mode;
    private int num=0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_control);

        context = this;
        setTitle("Home Control");

        ipAddr = (EditText) findViewById(R.id.editText_ip);

        room1switch = (Switch) findViewById(R.id.switch_room1);
        room2switch = (Switch) findViewById(R.id.switch_room2);
        room3switch = (Switch) findViewById(R.id.switch_room3);
        fanswitch = (Switch) findViewById(R.id.switch_fan);

        room1switch.setChecked(room1SW);
        room2switch.setChecked(room2SW);
        room3switch.setChecked(room3SW);
        fanswitch.setChecked(fanSW);

        resultData = (TextView) findViewById(R.id.textView_data1);
        resultData.setText("");

        room1switch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

                room1SW = isChecked;
                //mode = 0;
                Log.d(TAG, "num(SW) = "+num);

                if(isChecked)
                {
                    ledport = "27/on";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
                else
                {
                    ledport = "27/off";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
            }
        });

        room2switch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

                room2SW = isChecked;
                //mode = 0;

                if(isChecked)
                {
                    ledport = "22/on";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
                else
                {
                    ledport = "22/off";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
            }
        });

        room3switch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

                room3SW = isChecked;
                //mode = 0;

                if(isChecked)
                {
                    ledport = "23/on";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
                else
                {
                    ledport = "23/off";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
            }
        });

        fanswitch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {

                fanSW = isChecked;
                //mode = 0;

                if(isChecked)
                {
                    ledport = "24/on";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
                else
                {
                    ledport = "24/off";
                    ipAddrData = ipAddr.getText().toString();

                    sendURLData = new URLData();
                    sendURLData.execute();
                }
            }
        });

        room1ButtonON = (Button) findViewById(R.id.button_room1ON);
        room1ButtonOFF = (Button) findViewById(R.id.button_room1OFF);
        room2ButtonON = (Button) findViewById(R.id.button_room2ON);
        room2ButtonOFF = (Button) findViewById(R.id.button_room2OFF);
        room3ButtonON = (Button) findViewById(R.id.button_room3ON);
        room3ButtonOFF = (Button) findViewById(R.id.button_room3OFF);
        fanButtonON = (Button) findViewById(R.id.button_fanON);
        fanButtonOFF = (Button) findViewById(R.id.button_fanOFF);

        room1ButtonON.setOnClickListener(new roomButtonClick());
        room1ButtonOFF.setOnClickListener(new roomButtonClick());
        room2ButtonON.setOnClickListener(new roomButtonClick());
        room2ButtonOFF.setOnClickListener(new roomButtonClick());
        room3ButtonON.setOnClickListener(new roomButtonClick());
        room3ButtonOFF.setOnClickListener(new roomButtonClick());
        fanButtonON.setOnClickListener(new roomButtonClick());
        fanButtonOFF.setOnClickListener(new roomButtonClick());

    }

    private class roomButtonClick implements View.OnClickListener {
        @Override
        public void onClick(View v) {

            switch (v.getId())
            {
                case R.id.button_room1ON:
                    Log.d(TAG, "num = "+num);
                    if(ipAddr.length() != 0){
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "27/on";
                        Log.d(TAG, "ipaddrdata = "+ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }

                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        room1switch.setChecked(true);
                    break;

                case R.id.button_room1OFF:
                    if(ipAddr.length() != 0) {
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "27/off";
                        Log.d(TAG, "ipaddrdata = " + ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }
                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        room1switch.setChecked(false);
                    break;

                case R.id.button_room2ON:
                    if(ipAddr.length() != 0)
                    {
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "22/on";
                        Log.d(TAG, "ipaddrdata = "+ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }
                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        room2switch.setChecked(true);
                    break;

                case R.id.button_room2OFF:
                    if(ipAddr.length() != 0)
                    {
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "22/off";
                        Log.d(TAG, "ipaddrdata = "+ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }
                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        room2switch.setChecked(false);
                    break;

                case R.id.button_room3ON:
                    if(ipAddr.length() != 0)
                    {
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "23/on";
                        Log.d(TAG, "ipaddrdata = "+ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }
                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        room3switch.setChecked(true);
                    break;

                case R.id.button_room3OFF:
                    if(ipAddr.length() != 0)
                    {
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "23/off";
                        Log.d(TAG, "ipaddrdata = "+ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }
                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        room3switch.setChecked(false);
                    break;

                case R.id.button_fanON:
                    if(ipAddr.length() != 0)
                    {
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "24/on";
                        Log.d(TAG, "ipaddrdata = "+ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }
                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        fanswitch.setChecked(true);
                    break;

                case R.id.button_fanOFF:
                    if(ipAddr.length() != 0)
                    {
                        ipAddrData = ipAddr.getText().toString();
                        ledport = "24/off";
                        Log.d(TAG, "ipaddrdata = "+ipAddrData);

                        sendURLData = new URLData();
                        sendURLData.execute();
                    }
                    else
                        Toast.makeText(context, "Please input IP Address!", Toast.LENGTH_SHORT).show();
                        fanswitch.setChecked(false);
                    break;
            }

        }
    }

    private class URLData extends AsyncTask<Void, Void, String> {
        @Override
        protected String doInBackground(Void... voids) {
            String data = null;

                webURL = new StringBuilder();
                webURL.append(httpUrl);
                webURL.append(ipAddrData);
                webURL.append(webUrl);
                webURL.append(ledport);

                Log.d(TAG, "weburl = "+webURL);

                try{
                    url = new URL(webURL.toString());
                    Log.d(TAG, "url = "+url);

                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    conn.setRequestMethod("GET");

                    int code = conn.getResponseCode();
                    Log.d(TAG, "code = "+code);

                    if(code == HttpURLConnection.HTTP_OK)
                    {
                        InputStream input = conn.getInputStream();
                        InputStreamReader reader = new InputStreamReader(input);

                        char[] buffer = new char[100];
                        reader.read(buffer);
                        data = String.valueOf(buffer);

                        input.close();
                    }
                    else
                        data = null;

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
            Log.d(TAG,"weburl="+s);

        }
    }

}
