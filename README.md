# responsive-table-generator

This is a simple python script to generate responsive HTML tables.

# Usage
In your css file, insert the following media query along with any styles to the table.
```css
@media screen and (max-width: 616px){
  .responsive-table td:before{
    content: attr(data-label);
    float: left;
    text-transform: uppercase;
    font-size: 15px;
    letter-spacing: 1px;
    font-weight: 600;
    vertical-align: bottom;
    margin-right: 10px;
  }
}
```

To run the script, simply navigate to the script and run the following on the command line:
``` shell
  python gen.py
```
