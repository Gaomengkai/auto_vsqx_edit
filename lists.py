class convert_to_p():
    def __init__(self,pinyin):
        pinyin = chr(str(pinyin))
        per=['0','2','3','4']
        sign=1
        s_y='a'
        s_s='l'
        sheng_type=1
        sheng1=['b','p','m','f','d','t','n','l','g','k','h','j','q','x','r','z','c','s']
        s1=['p','p_h','m','f','t','t_h','n','l','k','k_h','x',"ts\\","ts\\_h",'s\\','z\'','ts','ts_h','s']
        sheng2=['zh','ch','sh']
        s2=['ts\'','ts\'_h','s\'']
        sheng3=['y','w']
        s3=['i','u']

        yun1_1=['a','o','e','i','u']
        yun2_y=['u','v']#About following j/q/x//n/l//y
        yun1_2=['er']
        yun2_i=['i']#About following z/c/s//zh/ch/sh
        yun1_3=['ai','ei','ao','ou','ia','ie','ua','uo']
        yun2_ue=['ue','ve']#About following j/q/x//n/l//y
        yun1_4=['iao','iu']
        pass
        
        if(pinyin[len(pinyin)-1] in per):
            sign=int(pinyin[len(pinyin)-1])
        if(pinyin[0] in sheng1):
            if(pinyin[1] == 'h'):
                sheng=str(pinyin[0])+str(pinyin[1])
                sheng_type=2
            else:
                sheng=str(pinyin[0])
                sheng_type=1
        elif(pinyin[0] in sheng3):
            sheng_type=3
        else:
            sheng_type=0

        if(sheng_type in [1,2]):
            s_s=sheng
        
