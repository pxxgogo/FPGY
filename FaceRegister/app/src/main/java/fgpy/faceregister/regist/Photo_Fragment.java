package fgpy.faceregister.regist;

import android.content.ContentResolver;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Matrix;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import java.io.FileNotFoundException;

import fgpy.faceregister.R;

public class Photo_Fragment extends Fragment {

    final int REQUEST_CODE_TAKE_PICTURE = 2;
    final int RESULT_LOAD_IMAGE = 4;
    String lastphototaken;
    View rootv;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        rootv = inflater.inflate(R.layout.fragment3_register, container, false);
        Button takephoto = (Button)rootv.findViewById(R.id.btn_take);
        takephoto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                callCamera();
            }
        });
        Button selectphoto = (Button)rootv.findViewById(R.id.btn_select);
        selectphoto.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectphoto();
            }
        });
        Button back = (Button)rootv.findViewById(R.id.btn_finish);
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                getActivity().finish();
            }
        });
        return rootv;
    }

    /*
    调用照相机
     */
    public void callCamera(){
        String state = Environment.getExternalStorageState(); //拿到sdcard是否可用的状态码
        if (state.equals(Environment.MEDIA_MOUNTED)){   //如果可用
            Intent intent = new Intent("android.media.action.IMAGE_CAPTURE");
            startActivityForResult(intent,REQUEST_CODE_TAKE_PICTURE);
        }else {
            Toast.makeText(getActivity().getApplicationContext(), "SD卡不可用", Toast.LENGTH_SHORT).show();
        }
    }
    /*
    选择图库数据
     */
    public void selectphoto(){
        Intent i = new Intent(
                Intent.ACTION_PICK, android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        startActivityForResult(i, RESULT_LOAD_IMAGE);
    }

    public void dispImg(Bitmap bm){
        ImageView imageView = (ImageView)rootv.findViewById(R.id.photodisp);
        int new_width = 300;
        int new_height = 400;

        int width = bm.getWidth();
        int height = bm.getHeight();
        float scaleWidth = ((float)new_width) / width;
        float scaleHeight = ((float)new_height) / height;
        float scale = (scaleHeight > scaleWidth) ? scaleWidth : scaleHeight;
        Matrix matrix = new Matrix();
        matrix.postScale(scale, scale);
        Bitmap resizedBitmap = Bitmap.createBitmap(bm, 0, 0, width,
                height, matrix, true);
        imageView.setImageBitmap(resizedBitmap);
    }
    /*
    接受相机返回的数据
     */
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {
        switch (requestCode){
            case REQUEST_CODE_TAKE_PICTURE:
                if (data.getData() != null|| data.getExtras() != null) { //防止没有返回结果
                    Uri uri = data.getData();
                    Bitmap photo = null;
                    if (uri != null) {
                        photo = BitmapFactory.decodeFile(uri.getPath()); //拿到图片
                    }
                    if (photo == null) {
                        Bundle bundle = data.getExtras();
                        if (bundle != null) {
                            photo = (Bitmap) bundle.get("data");
                            dispImg(photo);
                        } else {
                            Toast.makeText(getActivity().getApplicationContext(), "找不到图片", Toast.LENGTH_SHORT).show();
                        }
                    }
                }
                break;
            case RESULT_LOAD_IMAGE:
                if (data == null)
                    break;
                Uri uri = data.getData();
                ContentResolver cr = getActivity().getContentResolver();
                try {
                    Bitmap bitmap = BitmapFactory.decodeStream(cr.openInputStream(uri));
                    dispImg(bitmap);
                } catch (FileNotFoundException e) {
                    Log.e("Exception", e.getMessage(),e);
                }
                break;
            default:
                break;
        }
    }
}
