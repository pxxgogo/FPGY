package fgpy.faceregister.login;

import android.app.ActionBar;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.view.Menu;
import android.view.View;
import android.view.ViewConfiguration;
import android.widget.Button;

import java.lang.reflect.Field;

import fgpy.faceregister.R;

/**
 * A login screen that offers login via email/password.
 */
public class LoginActivity extends AppCompatActivity {

    /**
     * The {@link android.support.v4.view.PagerAdapter} that will provide
     * fragments for each of the sections. We use a
     * {@link FragmentPagerAdapter} derivative, which will keep every
     * loaded fragment in memory. If this becomes too memory intensive, it
     * may be best to switch to a
     * {@link android.support.v4.app.FragmentStatePagerAdapter}.
     */
    private LoginActivity.SectionsPagerAdapter mSectionsPagerAdapter;

    /**
     * The {@link ViewPager} that will host the section contents.
     */
    private static ViewPager mViewPager;

    View.OnClickListener ls1 = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            Button button = (Button)v;
            button.setBackground(getResources().getDrawable(R.drawable.ic_mode_edit_black_48dp));
            Button bt2 = (Button)findViewById(R.id.withcamera);
            bt2.setBackground(getResources().getDrawable(R.drawable.ic_portrait_white_48dp));
            button.setClickable(false);
            bt2.setClickable(true);
            mViewPager.setCurrentItem(0);
        }
    };

    View.OnClickListener ls2 = new View.OnClickListener(){
        @Override
        public void onClick(View v) {
            Button button = (Button)v;
            button.setBackground(getResources().getDrawable(R.drawable.ic_portrait_black_48dp));
            Button bt2 = (Button)findViewById(R.id.withusernname);
            bt2.setBackground(getResources().getDrawable(R.drawable.ic_mode_edit_white_48dp));
            button.setClickable(true);
            bt2.setClickable(false);
            mViewPager.setCurrentItem(1);
        }
    };

    public boolean onCreateOptionsMenu(Menu menu){
        if ((getSupportActionBar()) != null){
            getSupportActionBar().setDisplayShowTitleEnabled(false);
            getSupportActionBar().setCustomView(R.layout.login_actionbar);
            getSupportActionBar().setDisplayOptions(ActionBar.DISPLAY_SHOW_CUSTOM);

            Button bt1 = (Button)findViewById(R.id.withusernname);
            bt1.setOnClickListener(ls1);
            Button bt2 = (Button)findViewById(R.id.withcamera);
            bt2.setOnClickListener(ls2);
        }
        return true;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        //action bar里的按钮显示不出来
        try {
            ViewConfiguration mconfig = ViewConfiguration.get(this);
            Field menuKeyField = ViewConfiguration.class.getDeclaredField("sHasPermanentMenuKey");
            if(menuKeyField != null) {
                menuKeyField.setAccessible(true);
                menuKeyField.setBoolean(mconfig, false);
            }
        } catch (Exception ex) {
        }
        mSectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());
        mViewPager = (ViewPager)findViewById(R.id.container);
        mViewPager.setAdapter(mSectionsPagerAdapter);
        mViewPager.addOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {

            }

            @Override
            public void onPageSelected(int position) {
                Button username = (Button)findViewById(R.id.withusernname);
                Button camera = (Button)findViewById(R.id.withcamera);
                switch (position){
                    case 0:
                        username.setBackground(getResources().getDrawable(R.drawable.ic_mode_edit_black_48dp));
                        camera.setBackground(getResources().getDrawable(R.drawable.ic_portrait_white_48dp));
                        username.setClickable(false);
                        camera.setClickable(true);
                        break;
                    case 1:
                        username.setBackground(getResources().getDrawable(R.drawable.ic_mode_edit_white_48dp));
                        camera.setBackground(getResources().getDrawable(R.drawable.ic_portrait_black_48dp));
                        username.setClickable(true);
                        camera.setClickable(false);
                        break;
                    default:
                        break;
                }
            }

            @Override
            public void onPageScrollStateChanged(int state) {

            }
        });
    }


    /**
     * A {@link FragmentPagerAdapter} that returns a fragment corresponding to
     * one of the sections/tabs/pages.
     */
    public class SectionsPagerAdapter extends FragmentPagerAdapter {

        public SectionsPagerAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int position) {
            switch (position){
                case 0:
                    return UserNameFragment.newInstance(1);
                case 1:
                    return CameraFragment.newInstance(2);
            }
            return null;
        }

        @Override
        public int getCount() {
            return 2;
        }

        @Override
        public CharSequence getPageTitle(int position) {
            switch (position) {
                case 0:
                    return "UserName";
                case 1:
                    return "Camera";
            }
            return null;
        }

    }
}

