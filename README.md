# responsive-table-generator

This is a simple python script to generate responsive HTML tables.

# Demo
<style>
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
</style>
<table class='responsive-table' style="width: 0 auto;">
   <thead>
      <tr>
         <th>First</th>
         <th>Second</th>
         <th>Third</th>
         <th>Fourth</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td data-label='First'></td>
         <td data-label='Second'></td>
         <td data-label='Third'></td>
         <td data-label='Fourth'></td>     
      </tr>
      <tr>
         <td data-label='First'></td>
         <td data-label='Second'></td>
         <td data-label='Third'></td>
         <td data-label='Fourth'></td>      
      </tr>
      <tr>
         <td data-label='First'></td>
         <td data-label='Second'></td>
         <td data-label='Third'></td>
         <td data-label='Fourth'></td>      
      </tr>
      <tr>
         <td data-label='First'></td>
         <td data-label='Second'></td>
         <td data-label='Third'></td>
         <td data-label='Fourth'></td>      
      </tr>
      <tr>
         <td data-label='First'></td>
         <td data-label='Second'></td>
         <td data-label='Third'></td>
         <td data-label='Fourth'></td>      
      </tr>
      <tr>
         <td data-label='First'></td>
         <td data-label='Second'></td>
         <td data-label='Third'></td>
         <td data-label='Fourth'></td>      
      </tr>
   </tbody>
</table>
# Usage
In your css file, insert the following media query along with any additional styles to the table.
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
