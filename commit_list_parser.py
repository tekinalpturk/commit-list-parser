import string

input_str = """
"""

curLine = ""
lineCounter = 0
commit_code = ""
commit_desc = ""
commit_user = ""
commit_date = ""
print_for_excel = True
print_merge_commits = False
for idx, line in enumerate(input_str.splitlines()):
    if idx % 4 == 0:
        if ((not commit_desc.find('Merged PR') != -1) & (not commit_desc.find('Merge remote-tracking branch') != -1)) | print_merge_commits:
            if commit_code:
                if print_for_excel:
                    print(str(lineCounter) + "\t" + commit_code + "\t" + commit_date + "\t" + commit_user + "\t" + commit_desc)
                else:
                    print(str(lineCounter) + "\t" + commit_code + "\t" + commit_date + "\t" + commit_user + "\n\t" + commit_desc)
                    print("-----------------------------------------------------------------------------------------------")
            lineCounter += 1
        commit_code = line
    if idx % 4 == 1:
        commit_desc = line
    if idx % 4 == 2:
        commit_user = line
    if idx % 4 == 3:
        commit_date = line
# Last Line
if ((not commit_desc.find('Merged PR') != -1) & (not commit_desc.find('Merge remote-tracking branch') != -1)) | print_merge_commits:
    if print_for_excel:
        print(str(lineCounter) + "\t" + commit_code + "\t" + commit_date + "\t" + commit_user + "\t" + commit_desc)
    else:
        print(str(lineCounter) + "\t" + commit_code + "\t" + commit_date + "\t" + commit_user + "\n\t" + commit_desc)
        print("-----------------------------------------------------------------------------------------------")
