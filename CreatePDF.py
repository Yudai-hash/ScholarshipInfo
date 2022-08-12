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
    string1 = "scholar"
    string2 = ".pdf"
    ################
    
    #####関数呼び出さない#######
    ######PDFファイルを生成する###################
    file_name = d + string2 ##ファイル名を設定
    pdf = canvas.Canvas(file_name,pagesize=portrait(A4)) ##PDFを生成、サイズA4
    pdf.saveState() ##セーブ?初期化?

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

    #####文字を描写#########
    pdf.drawString(1*cm,26*cm,a)

    pdf.setFont('HGRGE',20) ##フォントの変更
    width,height = A4 ###A4用紙の紙
    pdf.drawCentredString(width/2,height-2*cm,'研究助成金')

    pdf.restoreState()
    pdf.save()

if __name__ == '__name__':
    Create_pdf(a)
