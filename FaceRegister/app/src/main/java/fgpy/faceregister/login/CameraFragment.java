package fgpy.faceregister.login;

import android.hardware.Camera;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.view.ViewGroup;

import fgpy.faceregister.R;

/**
 * Created by guotata on 2016/10/5.
 */
public class CameraFragment extends Fragment implements SurfaceHolder.Callback, Camera.PreviewCallback {

    /**
     * The fragment argument representing the section number for this
     * fragment.
     */
    private static final String ARG_SECTION_NUMBER = "section_number";
    Camera camera ;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        View rootv = inflater.inflate(R.layout.fragment2_login, container, false);
        SurfaceView view = (SurfaceView) rootv.findViewById(R.id.surface_view);
        view.getHolder().addCallback(this);
        view.getHolder().setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS);
        return rootv;
    }
    public void surfaceCreated(SurfaceHolder holder) {

    }

    public void surfaceChanged(SurfaceHolder holder, int format, int width,
                               int height) {
        try{
            camera = Camera.open();
            camera.setPreviewDisplay(holder);
            Camera.Parameters params = camera.getParameters();
            params.setPreviewSize(1000, 1000);
            camera.setDisplayOrientation(90);
            camera.setParameters(params);
            camera.startPreview() ;
            camera.setPreviewCallback(this);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    public void surfaceDestroyed(SurfaceHolder holder) {
        if(camera != null) {
            camera.setPreviewCallback(null) ;
            camera.stopPreview();
            camera.release();
        }
    }

    public void onPreviewFrame(byte[] data, Camera camera) {

    }

    public static CameraFragment newInstance(int sectionNumber) {
        CameraFragment fragment = new CameraFragment();
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, sectionNumber);
        fragment.setArguments(args);
        return fragment;
    }
}
