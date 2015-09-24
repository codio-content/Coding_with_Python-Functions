// This creates a special variable for reading files
fs = require('fs')

function convertField(str) {
  
  // isNan() checks if the field can be converted into a number
  if ( isNaN( str ) || str == '') {
    // Not a number, so replace |c with ,
    while ( (pos = str.indexOf('|c'))  != -1 ) {
      str = str.substring(0, pos) + ',' + str.substring(pos+2)
    }
  }
  else {
    // It can be converted into a number
    str = parseFloat( str )
  }    
  return str
}

function parseData() {

  // Go through all the rows
  for ( i=0, cols = []; i<rows.length; i++, cols = [] ) {
    // Create an array (cols) of fields for this row
    cols = rows[i].split(',')
    // Now loop through each field
    for ( j=0; j<cols.length; j++) {
      // Call our new function
      cols[j] = convertField( cols[j] )
    }
    rows[i] = cols
  }  
  return
}

//
// READ DATA.CSV
//
data = fs.readFileSync('data.csv').toString()
rows = data.split('\n')
parseData()
console.log('-----DATA.CSV')
console.log(rows)


//
// READ MORE-DATA.CSV
//
data = fs.readFileSync('more-data.csv').toString()
rows = data.split('\n')
parseData()
console.log('-----MORE-DATA.CSV')
console.log(rows)

