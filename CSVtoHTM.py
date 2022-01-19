import pandas as pd 
  
a = pd.read_csv("project.csv",error_bad_lines=False, encoding = "ISO-8859-1")
  
a.to_html("WebsiteProject.htm") 
  
html_file = a.to_html()