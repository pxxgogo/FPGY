package fgpy.faceregister.regist;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;

import fgpy.faceregister.R;

/**
 * A login screen that offers login via email/password.
 */
public class RegisterActivity extends AppCompatActivity {

    /**
     * The {@link android.support.v4.view.PagerAdapter} that will provide
     * fragments for each of the sections. We use a
     * {@link FragmentPagerAdapter} derivative, which will keep every
     * loaded fragment in memory. If this becomes too memory intensive, it
     * may be best to switch to a
     * {@link android.support.v4.app.FragmentStatePagerAdapter}.
     */
    private RegisterActivity.SectionsPagerAdapter mSectionsPagerAdapter;

    /**
     * The {@link ViewPager} that will host the section contents.
     */
    private static ViewPager mViewPager;
    //有效的最大页面
    private int validPosition = -1;
    //页面列表
    private List<Fragment> stepList;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        stepList = new ArrayList<Fragment>();

        mSectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());
        mViewPager = (ViewPager)findViewById(R.id.container);
        mViewPager.setAdapter(mSectionsPagerAdapter);
        mViewPager.addOnPageChangeListener(new ViewPager.OnPageChangeListener() {
            @Override
            public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {
                if (position > validPosition)
                    mViewPager.setCurrentItem(position);
            }

            @Override
            public void onPageSelected(int position) {
                if (position <= validPosition)
                    validPosition = position - 1;
                if (position == 2){
                    ((Photo_Fragment)stepList.get(2)).callCamera();
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
                    stepList.add(0,new UserName_ID_Fragment());
                    return stepList.get(0);
                case 1:
                    stepList.add(1,new Name_Pass_Fragment());
                    return stepList.get(1);
                case 2:
                    stepList.add(2, new Photo_Fragment());
                    return stepList.get(2);
            }
            return null;
        }

        @Override
        public int getCount() {
            // Show 3 total pages.
            return 3;
        }

        @Override
        public CharSequence getPageTitle(int position) {
            switch (position) {
                case 0:
                    return "UserName_ID";
                case 1:
                    return "Name_Pass";
                case 2:
                    return "Photo";
            }
            return null;
        }
    }

    public void gotoNextPage(){
        int page = mViewPager.getCurrentItem() + 1;
        mViewPager.setCurrentItem(page);
    }

    public void setValidPosition(int newpos){
        this.validPosition = newpos;
    }
}

