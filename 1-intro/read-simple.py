// This creates a special variable for reading files
fs = require('fs')

//
// READ DATA.CSV
//
data = fs.readFileSync('data.csv').toString()
rows = data.split('\n')

// Go through all the rows
for ( i=0, cols = []; i<rows.length; i++, cols = [] ) {
  // Create an array (cols) of fields for this row
  cols = rows[i].split(',')
  // Now loop through each field
  for ( j=0; j<cols.length; j++) {
    // isNan() checks if the field can be converted into a number
    if ( isNaN( cols[j]) || cols[j] == '' ) {
      // Not a number, so replace |c with ,
      while ( (pos = cols[j].indexOf('|c'))  != -1 ) {
        cols[j] = cols[j].substring(0, pos) + ',' + cols[j].substring(pos+2)
      }
    }
    else {
      // It can be converted into a number
      cols[j] = parseFloat(cols[j])
    }  
  }
  rows[i] = cols
}
console.log(rows)




