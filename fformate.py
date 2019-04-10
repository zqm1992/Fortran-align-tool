#test git
# -*-coding:utf-8-*-
import os
import re

path = "D:\\test\\dam\\code\\dam_break_withoutnonmatch"
files= os.listdir(path)

for file in files:
	if not os.path.isdir(file):
		match_f90	= re.match( r'.*\.f90', file, re.M|re.I)
		if(match_f90):
			file_obj 	= open(path+"\\"+file)
			all_lines 	= file_obj.readlines()
			f			= open(path+"\\new\\"+file,'w+')
			lev=1
			sp='  '
			linenum=0
			mark=0
			for line in all_lines:
				match_comment 	  	= re.match( r'[\s]*!', line, re.M|re.I)
				match_type		 	= re.match( r'[\s]*((\btype\b))', line, re.M|re.I)
				match_type_bra		= re.match( r'[\s]*((\btype\b))[\s]*\(', line, re.M|re.I)
				match_recst		 	= re.match( r'[\s]*((\bsubroutine\b)|(\bdo\b)|(\binterface\b)|(\bfunction\b)|(\bprogram\b)|(\blogical\b[\s]*(\bfunction\b)))', line, re.M|re.I)
				match_recen			= re.match( r'[\s]*((\bend))', line, re.M|re.I)
				match_if			= re.match( r'[\s]*((\bif\b))', line, re.M|re.I)
				match_if_then		= re.match( r'[\s]*((\bif\b))[^!]*(\bthen\b)', line, re.M|re.I)
				match_then			= re.match( r'[\s]*[^!]*(\bthen\b)', line, re.M|re.I)
				match_else			= re.match( r'[\s]*((\belse))', line, re.M|re.I)
				match_else_only		= re.match( r'[\s]*((\belse\b))', line, re.M|re.I)
				match_elseif_then	= re.match( r'[\s]*((\belseif\b))[^!]*(\bthen\b)', line, re.M|re.I)
				match_mod		 	= re.match( r'[\s]*((\bmodule\b))', line, re.M|re.I)
				match_mod_pro		= re.match( r'[\s]*((\bmodule\b))[\s]*((\bprocedure\b))', line, re.M|re.I)
				match_con			= re.match( r'[\s]*(?P<con>.*)', line, re.M|re.I)
		
				if(match_comment):
					if(match_con):
						mark=1
						linenum=linenum+1
						for space_num in range(lev):
							f.write(sp)
						f.write(match_con.group('con'))
						f.write('\n')
				elif(match_recst):
					mark=2
					linenum=linenum+1
					for space_num in range(lev):
						f.write(sp)
					f.write(match_con.group('con'))
					f.write('\n')
					lev=lev+1
				elif(match_recen):
					mark=3
					linenum=linenum+1
					lev=lev-1
					for space_num in range(lev):
						f.write(sp)
					f.write(match_con.group('con'))
					f.write('\n')
				elif(match_if):
					mark=4
					linenum=linenum+1
					for space_num in range(lev):
						f.write(sp)
					f.write(match_con.group('con'))
					f.write('\n')
					if(match_if_then):
						lev=lev+1
				elif(match_else):
					mark=5
					linenum=linenum+1
					if(match_else_only or match_elseif_then):
						lev=lev-1
						for space_num in range(lev):
							f.write(sp)
						f.write(match_con.group('con'))
						f.write('\n')
						lev=lev+1
					else:
						lev=lev-1
						for space_num in range(lev):
							f.write(sp)
						f.write(match_con.group('con'))
						f.write('\n')
				elif(match_then):
					mark=6
					linenum=linenum+1
					for space_num in range(lev):
						f.write(sp)
					f.write(match_con.group('con'))
					f.write('\n')
					lev=lev+1
				elif(match_mod):
					mark=7
					linenum=linenum+1
					for space_num in range(lev):
						f.write(sp)
					f.write(match_con.group('con'))
					f.write('\n')
					if(match_mod_pro):
						lev=lev
					else:
						lev=lev+1
				elif(match_type):
					mark=8
					linenum=linenum+1
					for space_num in range(lev):
						f.write(sp)
					f.write(match_con.group('con'))
					f.write('\n')
					if(match_type_bra):
						lev=lev
					else:
						lev=lev+1
				else:
					if(match_con):
						mark=9
						linenum=linenum+1
						for space_num in range(lev):
							f.write(sp)
						f.write(match_con.group('con'))
						f.write('\n')
				#print(mark)
			file_obj.close()		
#print(linenum)
