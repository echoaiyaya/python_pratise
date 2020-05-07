import pymysql
import re
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    db='book',
    user='root',
    passwd='123456',
    charset='utf8',
    use_unicode=True
)
cursor = conn.cursor()
sql = """select books_id, books_name, books_contribution from books order by books_create_date asc"""
cursor.execute(sql)
datas = cursor.fetchall()
for data in datas:
    dataid = data[0]
    booksName = data[1]
    booksIntro = data[2]
    cursor.execute("""select books_category_name, books_content from books_category where books_id = %s order by books_category_sort asc""", (dataid))
    cdatas = cursor.fetchall()
    fileName = r'F:\business\echoaiyaya_requ\txt' + '\\' + booksName + '.txt'
    f = open(fileName, 'a', encoding="utf-8")
    f.write(u'书名：'+ booksName + '\r\n')
    f.write(u'简介：'+ booksIntro)
    f.write('========================================================================')
    f.write('========================================================================\r\n\r\n')
    for cdata in cdatas:
        cname = cdata[0]
        ccontent = cdata[1]
        ccontent = ccontent.replace(r'<p>', '\0\0\0\0\0\0\0')
        ccontent = ccontent.replace(r'</p>', '\r\n\r\n')
        del_htmls = re.findall(r'(<.*?>)', ccontent, re.S)
        for del_html in del_htmls:
            ccontent = ccontent.replace(del_html, '')
        f.write('--------------------'+cname+'-----------------------\r\n')
        f.write(ccontent)
        f.write('---------------------------------------------------- \r\n\r\n')
    f.close()
cursor.close()