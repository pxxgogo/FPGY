package fgpy.faceregister;

import android.app.Application;
import android.content.Context;

/**
 * Created by guotata on 2016/10/5.
 */
public class MyApplication extends Application {
    private static Context context;
    public MyApplication(){
        super();
        context = this;
    }
    public static Context getContext(){
        return context;
    }
}

