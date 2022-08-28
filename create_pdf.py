from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
import  datetime

def create_pdf(a,b,c):
    ################

    
    ################
    ##ここで、その日の日付と時間を読み込んで、それをファイル名に入れたい(例:scholar20220626.pdf みたいに)
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta,'JST')
    now = datetime.datetime.now(JST)
    d = now.strftime('%Y%m%d%H%M%S')
    #print(repr(now))
    #print(now)
    #print(d)
    #string1 = "scholar"
    #string2 = ".pdf"
    ################
    
    #####関数呼び出さない#######
    ######PDFファイルを生成する###################
    file_name = d + ".pdf" ##ファイル名を設定
    pdf = canvas.Canvas(file_name,pagesize=portrait(A4)) ##PDFを生成、サイズA4
    pdf.saveState() ##セーブ?初期化?
    #print("saveState")

    ###############ここ必要？
    #pdf.setAuthor('OFFICE54')
    #pdf.setTitle('TEST')
    #pdf.setSubject('TEST')

    ###図形の描写####################
    #pdf.setFillColorRGB(54,54,0)
    #pdf.rect(1*cm,1*cm,4*cm,4*cm,stroke=1,fill=1)
    #pdf.setFillColorRGB(0,0,0)

    ####線の描写#########
    #pdf.setLineWidth(1)
    #pdf.line(10.5*cm,27*cm,10.5*cm,1*cm)

    ####フォントを設定##########
    pdfmetrics.registerFont(TTFont('HGRGE',"C:/Windows/Fonts/HGRGE.TTC"))
    pdf.setFont('HGRGE',12) #フォント初期化?
    #print("setFont")

    ########################
    #n = 0
    #####文字を描写#########
    
    #for i in range(0,20+1):
    #    if (len(a[i])>45):
    #        if n%2 == 0:
    #            pdf.drawString(1*cm,(26-n)*cm,a[i][:45])
    #            pdf.drawString(1*cm,(25.5-n)*cm,a[i][10:45])
    #            n = n + 1
    #        elif n%3 == 0:
    #            pdf.drawString(1*cm,(26-n)*cm,a[i][:45])
    #            pdf.drawString(1*cm,(25.5-n)*cm,a[i][10:45])
    #            n = n + 1
    #        else:
    #            pdf.drawString(1*cm,(26-n)*cm,a[i][:45])
    #            pdf.drawString(1*cm,(25.5-n)*cm,a[i][10:45])
    #            n = n + 1
                            
    #    elif(len(a[i])<=45):
    #        if n%2 == 0:
    #            pdf.drawString(1*cm,(26-0.5-0.5*n)*cm,a[i][:45])
    #            n = n + 1
    #        elif n%3 == 0:
    #            pdf.drawString(1*cm,(26-0.5-0.5*n)*cm,a[i][:45])
    #            n = n + 1
    #        else:
    #            pdf.drawString(1*cm,(26-0.5-0.5*n)*cm,a[i][:45])
    #            n = n + 1
        ##前段落を処理して、後付けで条件分岐を入れたほうが良いのでは
    pdf.drawString(1*cm,26*cm,a[0])
    pdf.drawString(1*cm,25.5*cm,a[1])
    pdf.drawString(1*cm,25*cm,a[2])
        
    pdf.drawString(1*cm,24*cm,a[3])
    pdf.drawString(1*cm,23.5*cm,a[4])
    pdf.drawString(1*cm,23*cm,a[5])

    pdf.drawString(1*cm,22*cm,a[6])
    pdf.drawString(1*cm,21.5*cm,a[7])
    pdf.drawString(1*cm,21*cm,a[8])

    pdf.drawString(1*cm,20*cm,a[9])
    pdf.drawString(1*cm,19.5*cm,a[10])
    pdf.drawString(1*cm,19*cm,a[11])

    pdf.drawString(1*cm,18*cm,a[12])
    pdf.drawString(1*cm,17.5*cm,a[13])
    pdf.drawString(1*cm,17*cm,a[14])

    pdf.drawString(1*cm,16*cm,a[15])
    pdf.drawString(1*cm,15.5*cm,a[16])
    pdf.drawString(1*cm,15*cm,a[17])

    pdf.drawString(1*cm,14*cm,a[18])
    pdf.drawString(1*cm,13.5*cm,a[19])
    pdf.drawString(1*cm,13*cm,a[20])

    pdf.drawString(1*cm,12*cm,a[21])
    pdf.drawString(1*cm,11.5*cm,a[22])
    pdf.drawString(1*cm,11*cm,a[23])

    pdf.drawString(1*cm,10*cm,a[24])
    pdf.drawString(1*cm,9.5*cm,a[25])
    pdf.drawString(1*cm,9*cm,a[26])
      
    pdf.drawString(1*cm,8*cm,a[27])
    pdf.drawString(1*cm,7.5*cm,a[28])
    pdf.drawString(1*cm,7*cm,a[29])

    pdf.drawString(1*cm,6*cm,a[30])
    pdf.drawString(1*cm,5.5*cm,a[31])
    pdf.drawString(1*cm,5*cm,a[32])

    pdf.drawString(1*cm,4*cm,a[33])
    pdf.drawString(1*cm,3.5*cm,a[34])
    pdf.drawString(1*cm,3*cm,a[35])   

    pdf.drawString(1*cm,2*cm,a[36])
    pdf.drawString(1*cm,1.5*cm,a[37])
    pdf.drawString(1*cm,1*cm,a[38])
    
    pdf.setFont('HGRGE',20) ##フォントの変更    
    width,height = A4 ###A4用紙の紙
    pdf.drawCentredString(width/2,height-2*cm,'研究助成金一覧 【'+c+'】')
    
    #pdf.restoreState()

    k = 39
    for i in range((b//13)-1): #(全件数÷dpf1ページに含まれる件数-1)-1は、pdf1ページはfor文に含まないからcountNumber/13)
        #-1しておく、最後のページ埋まらないから
        #(b//13)+1-1
        
        pdf.showPage()

        ####フォントを設定##########
        pdfmetrics.registerFont(TTFont('HGRGE',"C:/Windows/Fonts/HGRGE.TTC"))
        pdf.setFont('HGRGE',12) #フォント初期化?
        
        pdf.drawString(1*cm,26*cm,a[k])
        pdf.drawString(1*cm,25.5*cm,a[k+1])
        pdf.drawString(1*cm,25*cm,a[k+2])
        
        pdf.drawString(1*cm,24*cm,a[k+3])
        pdf.drawString(1*cm,23.5*cm,a[k+4])
        pdf.drawString(1*cm,23*cm,a[k+5])

        pdf.drawString(1*cm,22*cm,a[k+6])
        pdf.drawString(1*cm,21.5*cm,a[k+7])
        pdf.drawString(1*cm,21*cm,a[k+8])

        pdf.drawString(1*cm,20*cm,a[k+9])
        pdf.drawString(1*cm,19.5*cm,a[k+10])
        pdf.drawString(1*cm,19*cm,a[k+11])

        pdf.drawString(1*cm,18*cm,a[k+12])
        pdf.drawString(1*cm,17.5*cm,a[k+13])
        pdf.drawString(1*cm,17*cm,a[k+14])

        pdf.drawString(1*cm,16*cm,a[k+15])
        pdf.drawString(1*cm,15.5*cm,a[k+16])
        pdf.drawString(1*cm,15*cm,a[k+17])

        pdf.drawString(1*cm,14*cm,a[k+18])
        pdf.drawString(1*cm,13.5*cm,a[k+19])
        pdf.drawString(1*cm,13*cm,a[k+20])

        pdf.drawString(1*cm,12*cm,a[k+21])
        pdf.drawString(1*cm,11.5*cm,a[k+22])
        pdf.drawString(1*cm,11*cm,a[k+23])

        pdf.drawString(1*cm,10*cm,a[k+24])
        pdf.drawString(1*cm,9.5*cm,a[k+25])
        pdf.drawString(1*cm,9*cm,a[k+26])
      
        pdf.drawString(1*cm,8*cm,a[k+27])
        pdf.drawString(1*cm,7.5*cm,a[k+28])
        pdf.drawString(1*cm,7*cm,a[k+29])

        pdf.drawString(1*cm,6*cm,a[k+30])
        pdf.drawString(1*cm,5.5*cm,a[k+31])
        pdf.drawString(1*cm,5*cm,a[k+32])

        pdf.drawString(1*cm,4*cm,a[k+33])
        pdf.drawString(1*cm,3.5*cm,a[k+34])
        pdf.drawString(1*cm,3*cm,a[k+35])    

        pdf.drawString(1*cm,2*cm,a[k+36])
        pdf.drawString(1*cm,1.5*cm,a[k+37])
        pdf.drawString(1*cm,1*cm,a[k+38]) #39+38=77
        

        k = k + 39 #78-39=39
    
    

    pdf.save()
    #print("save")































