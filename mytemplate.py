# _*_ coding: utf-8 _*_
'''
#@Time  :2018-12-05;16:52
@author: aLuren

#@FileName: mytemplate.py
#@Software: PyCharm
Copyright(C)2018 SZ-MB-QTC
'''


# _*_ coding: utf-8 _*_
'''
#@Time  :${YEAR}-${MONTH}-${DAY};${TIME}
@author: aLuren

#@FileName: ${NAME}.py
#@Software: ${PRODUCT_NAME}
Copyright(C)${YEAR} SZ-MB-QTC
'''


'''
这是VSCode的template
{
	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"Print to console": {
			"prefix": "pythontemplates",
		 	"body": [
				"#!/usr/bin/python",
	            "#_*_coding: utf-8 _*_",
	            "'''",
				"@uthor:Julylun",
	            "Copyright(c)2019 SZ_MB-QTC",
	            "FileName:${TM_FILENAME}",
				"@DATE:${CURRENT_YEAR}-${CURRENT_MONTH_NAME_SHORT}-${CURRENT_DATE};${CURRENT_DAY_NAME_SHORT}",
				"@TIME:${CURRENT_HOUR}:${CURRENT_MINUTE}:${CURRENT_SECOND}",
				"'''",
				"",
	        ],
	        "description": "A Python file template."
 	}
}    
'''