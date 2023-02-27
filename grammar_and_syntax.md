# Cross
## Syntax
Similar to java, the structure of the language is class-based, with python-like methods such as ```__init__``` and other expansions such as ```__idx__``` and ```__format__```. 

A demonstration of a Hello World program can be seen below
```
|include <stdlib> as *
|include <stdio> as *
class main implements runtime {
  public static func main(int argc, char** argv) => int {
    out.println("Hello, World");
    return 0;
  }
}
```
Lets break it down

the ```|include ...``` statements are started with '|' characters. these serve similar function to the C pre-processor, and indicate to the interpreter that a keyword / file must be defined or included. inside these pre-processor 