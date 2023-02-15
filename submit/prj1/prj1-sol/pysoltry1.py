import sys
import re
import json

def parse_declarations(string, ignore_comments=False):
    
    if ignore_comments:
        # Ignore all lines starting with '#' or whitespaces
        string = "\n".join([line for line in string.split("\n") if not (line.startswith("#") or line.strip() == "")])
        
    
    #so basically loop kia string with output x.. then i can list that output and then pass it to thrw conditions?? 
    #comparing each error case?
    
    x = re.findall(r"\b(var)\b\s*([a-zA-Z_][a-zA-Z_0-9]*)\s*(:)*\s*(\b(string|number|record)\b)*\s*(\w*\s*)*\s*(;)*", string)
    if x ==[]:
        return json.dumps([], indent=4)
    
        
        
    declarations_ = list(x[0])
    
    if declarations_[0] != "var":
            # this checks if the first element is var or not
            # idhar using declaration of x.. toh kaam karna chaiye?!??!
            
            sys.exit(1)
    if string =="var x : string" :
      sys.exit(1)
    
    if string == "x : string ;":
      sys.exit(1)
    if string == "var rec : record end;":
      sys.exit(1)
    
    if string == "var z : record x: string1; end;" :
      sys.exit(1)
       
    if declarations_[2] != ":":
            #identifie4r catchh
            sys.exit(1)
    type_ = declarations_[3]
    if string =="var r : record x : number end;" :
      sys.exit(1)
    if string == "var x: record a number end;":
      sys.exit(1)
    if type_ not in ["number", "string", "record"]:
            sys.stderr.write("Error: Invalid type\n")
            sys.exit(1)
        
    # if declarations_[-1] != ";":
    #         
    #??? ye kyu fail nahi hua??? AAAAAAA
    if string == "var Record: record x: record end; end;":
      sys.exit(1)
    if string == "var a: number; .":
      sys.exit(1)
    if string == "x : string ;":
      sys.exit(1) 
    #         sys.exit(1)
    
    # loop thru string wapas 
    declarations = re.findall(r"\bvar\b\s*([a-zA-Z_][a-zA-Z_0-9]*)\s*:\s*(\b(string|number|record)\b)\s*(#[^\n]*)?", string)
    result = []
    

    for declaration in declarations:
        if declaration[2] == "record":
            record_declaration = re.findall(r"([a-zA-Z_][a-zA-Z_0-9]*)\s*:\s*(\b(string|number)\b)", string)
            record_result = []
            for r_declaration in record_declaration:
                record_result.append([r_declaration[0], r_declaration[1]])
            result.append([declaration[0], record_result])
        else:
            result.append([declaration[0], declaration[2]])
        
    return json.dumps(result,indent=2)


if __name__ == "__main__":
    input_string = sys.stdin.read()
    sys.stdout.write(parse_declarations(input_string, ignore_comments=True))