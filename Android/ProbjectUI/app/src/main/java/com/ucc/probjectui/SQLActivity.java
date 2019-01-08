package com.ucc.probjectui;

import android.app.Activity;
import android.content.Context;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;


public class SQLActivity extends Activity {

    private static final String TAG = "main";
    private Context context;
    private EditText editID, editName, editQuantity, editIPsql;
    private Button addButton, updateButton, delButton, selectButton;
    private String NameData;
    private String QuantityData;
    private UpdateSQLData myUpdateData;
    private String IdData;
    private GetSQLData mySelectData;
    private StringBuilder sqlURL;
    private int actionFlag;
    private TextView textViewResult;
    private URL url;

    private final int AddDataGet = 1;
    private final int UpdateData = 2;
    private final int DeleteData = 3;
    private final int SelectData = 4;

    private String http = "http://";
    private String port = ":5000/";
    private String seletDataURL = "select_data";
    private String deleteDataURL = "delete_data?";
    private String updateDataURL = "update_data?";
    private String addGetURL = "add_data?";

    private String addID = "id=";
    private String addName = "name=";
    private String addQuantity = "quantity=";
    private String dot = "&";
    private String sqlData;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sql);

        context = this;
        actionFlag = SelectData;

        editIPsql = (EditText) findViewById(R.id.editText_ipsql);

        editID = (EditText) findViewById(R.id.editText_id);
        editName = (EditText) findViewById(R.id.editText_name);
        editQuantity = (EditText) findViewById(R.id.editText_quantity);

        addButton = (Button) findViewById(R.id.button_add);
        updateButton = (Button) findViewById(R.id.button_update);
        delButton = (Button) findViewById(R.id.button_del);
        selectButton = (Button) findViewById(R.id.button_select);

        addButton.setOnClickListener(new buttonOnClick());
        updateButton.setOnClickListener(new buttonOnClick());
        delButton.setOnClickListener(new buttonOnClick());
        selectButton.setOnClickListener(new buttonOnClick());

        textViewResult = (TextView) findViewById(R.id.textView_result);
        textViewResult.setText("");
    }

    private class buttonOnClick implements View.OnClickListener {
        @Override
        public void onClick(View v) {

            switch (v.getId())
            {
                case R.id.button_add:
                    actionFlag = AddDataGet;
                    sqlData = editIPsql.getText().toString();

                    if(editName.length() != 0)
                    {
                        NameData = editName.getText().toString();
                        if(editQuantity.length() != 0)
                        {
                            QuantityData = editQuantity.getText().toString();

                            myUpdateData = new UpdateSQLData();
                            myUpdateData.execute();
                        }
                        else
                            Toast.makeText(context,"Please input your quantity.",Toast.LENGTH_SHORT).show();
                    }
                    else
                        Toast.makeText(context,"Please input your name.",Toast.LENGTH_SHORT).show();

                    break;

                case R.id.button_update:
                    actionFlag = UpdateData;
                    sqlData = editIPsql.getText().toString();

                    if(editID.length() != 0)
                    {
                        IdData = editID.getText().toString();
                        if(editName.length() != 0)
                        {
                            NameData = editName.getText().toString();
                            if(editQuantity.length() != 0)
                            {
                                QuantityData = editQuantity.getText().toString();

                                myUpdateData = new UpdateSQLData();
                                myUpdateData.execute();
                            }
                            else
                                Toast.makeText(context,"Please input your quantity.",Toast.LENGTH_SHORT).show();
                        }
                        else
                            Toast.makeText(context,"Please input your name.",Toast.LENGTH_SHORT).show();
                    }
                    else
                    {
                        Toast.makeText(context,"Please input your id number.",Toast.LENGTH_SHORT).show();
                    }

                    break;

                case R.id.button_del:
                    actionFlag = DeleteData;
                    sqlData = editIPsql.getText().toString();

                    if(editID.length() != 0)
                    {
                        IdData = editID.getText().toString();
                        //textViewResult.setText("");
                        mySelectData = new GetSQLData();
                        mySelectData.execute();

                    }
                    else
                    {
                        Toast.makeText(context,"Please input your id number.",Toast.LENGTH_SHORT).show();

                    }

                    break;

                case R.id.button_select:
                    actionFlag = SelectData;
                    sqlData = editIPsql.getText().toString();

                    textViewResult.setText("");
                    mySelectData = new GetSQLData();
                    mySelectData.execute();     //call mySelectData method()

                    break;
            }

        }
    }


    private class UpdateSQLData extends AsyncTask<Void, Void, String> {
        @Override
        protected String doInBackground(Void... voids) {
            String data = null;

            String param;

            sqlURL = new StringBuilder();
            sqlURL.append(http);
            sqlURL.append(sqlData);
            sqlURL.append(port);

            if(actionFlag == UpdateData)
            {
                param = updateDataURL+addID+IdData+dot+addName+NameData+dot+addQuantity+QuantityData;
                sqlURL.append(param);
            }
            else
            {
                param = addGetURL+addName+NameData+dot+addQuantity+QuantityData;
                sqlURL.append(param);
            }

            Log.d(TAG, "ip="+sqlURL);

            try{
                url = new URL(sqlURL.toString());
                Log.d(TAG,"url = "+url);

                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");

                int code = conn.getResponseCode();
                Log.d(TAG,"code = "+code);

                if(code == HttpURLConnection.HTTP_OK)
                {
                    InputStream input = conn.getInputStream();
                    InputStreamReader reader = new InputStreamReader(input);

                    char[] buffer = new char[100];
                    reader.read(buffer);
                    data = String.valueOf(buffer);

                    input.close();
                }

            } catch (MalformedURLException e){
                e.printStackTrace();

            } catch (IOException e){
                e.printStackTrace();

            }

            return data;
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            textViewResult.setText(s);
        }
    }

    private class GetSQLData extends AsyncTask<Void, Void, String> {
        @Override
        protected String doInBackground(Void... voids) {
            String data = null;

            sqlURL = new StringBuilder();
            sqlURL.append(http);
            sqlURL.append(sqlData);
            sqlURL.append(port);

            switch (actionFlag)
            {
                case SelectData:
                    sqlURL.append(seletDataURL);

                    break;

                case DeleteData:
                    sqlURL.append(deleteDataURL);
                    sqlURL.append(addID);
                    sqlURL.append(IdData);

                    break;

            }

            Log.d(TAG, "ip="+sqlURL);

            try{
                url = new URL(sqlURL.toString());
                Log.d(TAG, "url = "+url);
                HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                conn.setRequestMethod("GET");

                int code = conn.getResponseCode();
                Log.d(TAG,"code = "+code);

                if(code == HttpURLConnection.HTTP_OK)
                {
                    InputStream input = conn.getInputStream();
                    InputStreamReader reader = new InputStreamReader(input);
                    if(actionFlag == SelectData)
                    {
                        BufferedReader stringReader = new BufferedReader(reader);
                        data = stringReader.readLine();
                    }
                    else
                    {
                        char[] buffer = new char[100];
                        reader.read(buffer);
                        data = String.valueOf(buffer);
                    }

                    input.close();
                }
                else
                    data = null;


            } catch (MalformedURLException e){
                e.printStackTrace();

            } catch (IOException e) {
                e.printStackTrace();
            }

                return data;
        }

        @Override
        protected void onPostExecute(String s) {
            super.onPostExecute(s);

            if(actionFlag == SelectData) {
                if(s != null) {

                    try {

                        JSONArray jsonArray = new JSONArray(s);
                        int number = jsonArray.length();
                        Log.d(TAG, "array length = " + number);

                        StringBuilder jsonData = new StringBuilder();
                        for (int i = 0; i < number; i++) {
                            JSONObject jsonObj = jsonArray.getJSONObject(i);        //catch json data of each object
                            Log.d(TAG, "jsonObj = " + jsonObj);

                            int myID = jsonObj.getInt("id");
                            jsonData.append("id = " + myID + " , ");

                            String myUserName = jsonObj.getString("name");
                            jsonData.append("name = " + myUserName + " , ");

                            String myQuantity = jsonObj.getString("quantity");
                            jsonData.append("quantity = " + myQuantity + "\n");

                        }

                        textViewResult.append(jsonData.toString());

                    } catch (JSONException e) {

                        e.printStackTrace();
                    }

                }
                else
                    Toast.makeText(context,"There is no data.",Toast.LENGTH_SHORT).show();
            }
            else
                textViewResult.setText(s);
        }
    }
}
