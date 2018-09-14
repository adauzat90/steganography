from PIL import Image
import random

def encodeInfo(Image,Info,startingSeed):
    
    seed_list = []
    seed_ind = 0
    random.seed(startingSeed)
    new_seed = random.randrange(1000000000)
    seed_list.append(new_seed)
    
    startingRandomState = random.getstate()
    
    new_img = []
    flattened_info = [y for x in Info for y in x]
    px_index = 0
    
    
    for info in flattened_info:
        try:
            red_c = int(info / 100)
            green_c = int((info % 100)/10)
            blue_c = info % 10
            
            new_px = [Image[px_index][0],Image[px_index][1],Image[px_index][2]]
            new_px2 = [Image[px_index+1][0],Image[px_index+1][1],Image[px_index+1][2]]
            
            difference = abs((new_px[0]%10) - (new_px2[0]%10))
                
            if (difference - red_c) < 0:
                for _ in xrange(abs((difference - red_c))):
                    rand = random.randrange(0,2)
                    if rand == 0:
                        new_px[0]+=1
                    else:
                        new_px2[0]+=1
            if (difference - red_c) > 0:
                    for _ in xrange(abs((difference - red_c))):
                        rand = random.randrange(0,2)
                        if rand == 0:
                            new_px[0]-=1
                        else:
                            new_px2[0]-=1
                    
            difference = abs((Image[px_index][1]%10) - (Image[px_index+1][1]%10))
            if (difference - green_c) < 0:
                for _ in xrange(abs((difference - green_c))):
                    rand = random.randrange(0,2)
                    if rand == 0:
                        new_px[1]+=1
                    else:
                        new_px2[1]+=1
            if (difference - green_c) > 0:
                    for _ in xrange(abs((difference - green_c))):
                        rand = random.randrange(0,2)
                        if rand == 0:
                            new_px[1]-=1
                        else:
                            new_px2[1]-=1
            
            difference = abs((Image[px_index][2]%10) - (Image[px_index+1][2]%10))                
            if (difference - blue_c) < 0:
                for _ in xrange(abs((difference - blue_c))):
                    rand = random.randrange(0,2)
                    if rand == 0:
                        new_px[2]+=1
                    else:
                        new_px2[2]+=1
            if (difference - blue_c) > 0:
                    for _ in xrange(abs((difference - blue_c))):
                        rand = random.randrange(0,2)
                        if rand == 0:
                            new_px[2]-=1
                        else:
                            new_px2[2]-=1   
                            
            px_index += 2
            new_px = (new_px[0],new_px[1],new_px[2])
            new_px2 = (new_px2[0],new_px2[1],new_px2[2])
            new_img.append(new_px)
            new_img.append(new_px2)
        except:
            
            seed_ind+=1
            random.setstate(startingRandomState)
            new_seed = random.randrange(1000000000)
            print "setting new seed:" +str(new_seed)
            seed_list.append(new_seed)
            startingRandomState = random.getstate()
            random.seed(new_seed)
            
            px_index = 0
            
    for _ in xrange(10):
        print "Putting ending 0's"
        random.setstate(startingRandomState)
        new_seed = random.randrange(1000000000)
        seed_list.append(new_seed)
        startingRandomState = random.getstate()
        random.seed(new_seed)            
        
        try:
            blue_c = 0
            new_px = [Image[px_index][0],Image[px_index][1],Image[px_index][2]]
            new_px2 = [Image[px_index+1][0],Image[px_index+1][1],Image[px_index+1][2]]
            difference = abs((new_px[2]%10) - (new_px2[2]%10))   
            if (difference - blue_c) < 0:
                for _ in xrange(abs((difference - blue_c))):
                    rand = random.randrange(0,2)
                    if rand == 0:
                        new_px[2]+=1
                    else:
                        new_px2[2]+=1
            if (difference - blue_c) > 0:
                    for _ in xrange(abs((difference - blue_c))):
                        rand = random.randrange(0,2)
                        if rand == 0:
                            new_px[2]-=1
                        else:
                            new_px2[2]-=1
            
                
            new_px = (new_px[0],new_px[1],new_px[2])
            new_px2 = (new_px2[0],new_px2[1],new_px2[2])                
            new_img.append(new_px)
            new_img.append(new_px2)
            seed_ind+=2
            
        except:
            pass
            
    return seed_list, new_img


def decodeInfo(Image,seedList):
    seedList = seedList.reverse()
    seed_ind = 0
    random.seed(seedList[seed_ind])
    new_img = []

    px_index = 0
    
    blue_counter = 0
    end_counter = 0
    try:
        while blue_counter != 10:
            difference = abs((Image[px_index][2]%10) - (Image[px_index+1][2]%10))
            if difference == 0:
                blue_counter+=1
            end_counter+=1
        
    except:
        pass
    
    end_of_info = end_counter - blue_counter
    
    for index in xrange(end_of_info):
        pass
    
    
    for seed in seedList: #Not correct
        try:
            
            new_px = [Image[px_index][0],Image[px_index][1],Image[px_index][2]]
            new_px2 = [Image[px_index+1][0],Image[px_index+1][1],Image[px_index+1][2]]
            
            red = abs((new_px[0]%10) - (new_px2[0]%10))
            green = abs((new_px[1]%10) - (new_px2[1]%10))
            blue = abs((new_px[2]%10) - (new_px2[2]%10))
            
            info_px = (red,green,blue)
            
            difference = abs((new_px[0]%10) - (new_px2[0]%10))
                
            if (difference - red_c) < 0:
                for _ in xrange(abs((difference - red_c))):
                    rand = random.randrange(0,1)
                    if rand == 0:
                        new_px[0]+=1
                    else:
                        new_px2[0]+=1
            if (difference - red_c) > 0:
                    for _ in xrange(abs((difference - red_c))):
                        rand = random.randrange(0,1)
                        if rand == 0:
                            new_px[0]-=1
                        else:
                            new_px2[0]-=1
                    
            difference = abs((Image[px_index][1]%10) - (Image[px_index+1][1]%10))
            if (difference - green_c) < 0:
                for _ in xrange(abs((difference - green_c))):
                    rand = random.randrange(0,1)
                    if rand == 0:
                        new_px[1]+=1
                    else:
                        new_px2[1]+=1
            if (difference - green_c) > 0:
                    for _ in xrange(abs((difference - green_c))):
                        rand = random.randrange(0,1)
                        if rand == 0:
                            new_px[1]-=1
                        else:
                            new_px2[1]-=1
            
            difference = abs((Image[px_index][2]%10) - (Image[px_index+1][2]%10))                
            if (difference - blue_c) < 0:
                for _ in xrange(abs((difference - blue_c))):
                    rand = random.randrange(0,1)
                    if rand == 0:
                        new_px[2]+=1
                    else:
                        new_px2[2]+=1
            if (difference - blue_c) > 0:
                    for _ in xrange(abs((difference - blue_c))):
                        rand = random.randrange(0,1)
                        if rand == 0:
                            new_px[2]-=1
                        else:
                            new_px2[2]-=1   
                            
            px_index += 2
            new_px = (new_px[0],new_px[1],new_px[2])
            new_px2 = (new_px2[0],new_px2[1],new_px2[2])
            new_img.append(new_px)
            new_img.append(new_px2)
        except:
            seed_ind+=1
            random.seed(seedList[seed_ind])
            px_index = 0
    return new_img

if __name__ == "__main__":
    
    encoderImage = Image.open("huskyPup.png")
    pic_width, pic_height = encoderImage.size
    px = encoderImage.getdata()
    print (px[1][0])
    encodingInfo = Image.open("husky-puppies-01.jpg")
    data = encodingInfo.getdata()
    data = list(data)
    
    seedList, encoded_img_pxs = encodeInfo(px,data,12345)
    
    seed_file = open('seedList','w')
    
    for seed in seedList:
        seed_file.write(str(seed))
    
    im = Image.new("RGB", (pic_width, pic_height))
    pix = im.load()
    for x in range(pic_width):
        for y in range(pic_height):
            pix[x,y] = encoded_img_pxs[pic_width*y + x]

    im.save("test.png", "PNG")
    
    
    
    
    #x = encodingInfo.read(1)
    #while x:
     #   y = '{0:08b}'.format(ord(x))
      #  print y
       # x = encodingInfo.read(1)
    
    