from pylab import *
from PIL import Image
import mahotas
import skimage.color
import scipy


def orcodeall(file_path,ax,total_image,pass_count,reject_count):
    def rgb2gray():
        return uint8(0.299*R + 0.587*G + 0.114*B)
    image2= Image.open(file_path)
    bitmap2= array(image2)
    
    resize_factor=0.25
    newsize=(round(image2.width*resize_factor) ,round(image2.height*resize_factor)  )

    image2=image2.resize(newsize)
    bitmap2= array(image2)
    # orange7
    y1=183
    y2=668
    x1=72
    x2=564
    # orange8 Rergion of interest [200 400 203 400]
    y1=200
    y2=400
    x1=203
    x2=400



    bitmap3=bitmap2#[y1:y2,x1:x2, :]
    R=bitmap3[:,:,0]
    G=bitmap3[:,:,1]
    B=bitmap3[:,:,2]
    grayImage=rgb2gray()

    image_hsv= skimage.color.rgb2hsv(bitmap2)
    H= image_hsv[:,:,0]
    S= image_hsv[:,:,1]
    V= image_hsv[:,:,2]
    G=ones((3,3))*(1/9)
    S=scipy.signal.convolve2d(S, G, mode='full', boundary='fill', fillvalue=0)

    ROI=S > 0.6


    #threshold1=80
    ImOrange=ROI#grayImage>=threshold1
    #figure(1);imshow(ImOrange,cmap='gray');show();dfggdfdtgr
    ImL,n=mahotas.label(ImOrange,ones((3,3),dtype=int))

    #figure(1);imshow(ImL,cmap='tab20');show();dfggdfdtgr

    

    
    ax.imshow(bitmap2)
    
    #total_image = 0
    #pass_count = 0
    #reject_count = 0
    
    for i in range(1,amax(ImL)+1):    
        r,c=where(ImL==i)
        x1=min(c)
        y1=min(r)
        w=max(c)-x1
        h=max(r)-y1
        x2=x1+w
        y2=y1+w
        if((w*h)>90000):
            total_image +=1
            SubImage=image_hsv[y1:y2,x1:x2,:]

            SubImage_H= SubImage[:,:,0]
            SubImage_S= SubImage[:,:,1]
            #figure(1);subplot(1,2,1);imshow(SubImage_H,cmap='gray');subplot(1,2,2);imshow(SubImage_S,cmap='gray');show();dfggdfdtgr
            
            ROI=SubImage_S > 0.7 
            
            #0.3/0.5
            #figure(10);imshow(ROI,cmap='gray');show();sdfsfgfsd
            
            BadArea=SubImage_H> 0.5
            #figure(10);imshow(BadArea,cmap='gray');show();sdfsfgfsd

            BadROI=ROI*BadArea
            #figure(10);imshow(BadROI,cmap='gray');show();sdfsfgfsd

            OrangeSize= sum(ROI)
            BadSize=sum(BadROI)
            BadRatio= (BadSize/OrangeSize)*100
            print(BadRatio)
    #        figure()
    #        imshow(BadROI,cmap='gray')
    #        text(10,10,str(r.size))
            if(BadRatio>5):
                reject_count +=1
                #text((x1+x2)/2,(y1+y2)/2,"Reject"+str(w*h),color='r')
                text((x1+x2)/2,(y1+y2)/2,"Reject",color='r',fontsize=20)
                overlay=Rectangle((x1,y1),w,h,edgecolor='r',facecolor='none',linewidth=4)
            
            else:
                pass_count +=1
                #text((x1+x2)/2,(y1+y2)/2,"Pass"+str(w*h),color='g')
                text((x1+x2)/2,(y1+y2)/2,"Pass",color='g',fontsize=20)
                overlay=Rectangle((x1,y1),w,h,edgecolor='g',facecolor='none',linewidth=4)
            ax.add_patch(overlay)
        
    

    
   
    return total_image,pass_count,reject_count


