# windows cli : python portconnecormdtov2.py
# 
# to incorporate the original connector authentication md into the v2 connector md
#
# overview
# for each md file in pages/connector-authentication
#   create an md file in pages/v1/connector-authentication
#   parse the front matter 
#   frontmatter = false;
#   while read line
#   if line starts with "---" and frontmatter === false
#		frontmatter = true;
#   elseif line starts with "---" and frontmatter = true
#		frontmatter = false;
#   
#   if frontmatter
#   	get first word before colon
#		v1_var = text after colon
#   else
#   copy the current line to output file
# endif
# close current file
# end foreach
# 

# will require manual amends to correct any discrepancies between the file names - there are inconsistencies in the v1 file naming
# 
# once all files created , amend :
# - _bin/v2/assets/
# - _includes/v2/connector/connector.html 
# - getconnectorscontent.py 
# to search for corresponding pages/v1/connector-authentication file  and incorporate the md into the new md files
# copy the contents of the file to the 
# NB: exclude the pages/v1/connector-authentication from the docker build
# any other exclusions?