package com.ucc.probjectui;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.Context;
import android.content.Intent;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Set;

public class MainActivity extends AppCompatActivity {

    private static final int REQUEST_ENABLE_BT = 100;
    private static final String TAG = "main";
    private Context context;
    private ListView btlistView;
    private BluetoothAdapter btAdapter;
    private Set<BluetoothDevice> allBTDevice;
    private ArrayList<String> btDeviceList;
    private ArrayAdapter<String> adapter;
    private String listData;
    private int mode;
    private int homeView = 1;
    private int homeControl = 2;
    private Intent intent;
    private ImageView homeControlImage, homeViewImage, sqlImage, webCameraImage;
    private EditText ipAddr;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        context = this;

        homeControlImage = (ImageView) findViewById(R.id.imageButton_homeControl);
        homeViewImage = (ImageView) findViewById(R.id.imageButton_homeView);
        sqlImage = (ImageView) findViewById(R.id.imageButton_sql);
        webCameraImage = (ImageView) findViewById(R.id.imageButton_camera);

        homeControlImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                intent = new Intent(context, homeControlActivity.class);
                startActivity(intent);

            }
        });

        homeViewImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                intent = new Intent(context, homeViewActivity.class);
                startActivity(intent);

            }
        });

        sqlImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                intent = new Intent(context, SQLActivity.class);
                startActivity(intent);
            }
        });

        webCameraImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                intent = new Intent(context, webViewActivity.class);
                startActivity(intent);
            }
        });

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);

        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu, menu);

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        switch (item.getItemId())
        {
            case R.id.bt_update:
                allBTDevice = btAdapter.getBondedDevices();
                btDeviceList.clear();

                if(allBTDevice.size() > 0)
                {
                    for(BluetoothDevice device : allBTDevice)
                    {
                        btDeviceList.add("paired : "+device.getName()+"\n"+device.getAddress());
                    }
                    //adapter.notifyDataSetChanged(); //device data update
                    adapter = new ArrayAdapter<String>(context, R.layout.simple_list_item_1, btDeviceList);
                    btlistView.setAdapter(adapter);
                }
                break;

            case R.id.bt_view:
                intent = new Intent(context, webViewActivity.class);
                startActivity(intent);
                break;

            case R.id.bt_control:

                break;

        }

        return super.onOptionsItemSelected(item);
    }


}
