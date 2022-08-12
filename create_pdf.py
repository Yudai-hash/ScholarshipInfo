from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import cm
from reportlab.pdfbase.ttfonts import TTFont
import  datetime

def create_pdf(a):
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

    #####文字を描写#########
    for i in range(1,1+1):
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

        
        
    pdf.setFont('HGRGE',20) ##フォントの変更    
    width,height = A4 ###A4用紙の紙
    pdf.drawCentredString(width/2,height-2*cm,'研究助成金一覧 【医療・介護】')

    #pdf.restoreState()
    pdf.save()
    #print("save")



