string = '<sp t="16" p0="%s" p1="5300" p2="0" p3="0" p4="2" p5="15" p6="1" p8="100"><p7><![CDATA[%s]]></p7></sp>'

for i in range(139):
	print string % (500+(i*50),str(13.8-i/10.0))
