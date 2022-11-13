//References resources in memory by providing the location itself. Allows for modifications without return.
pub fn run(){

   //primitive array
   let array1 = [1,2,3];
   let array2 = array1;

   println!("\nValues: {:?}", (array1, array2));

   /*From docs re: non-primitive value referencing: 
      "If you assign another variable to a piece of data, the first variable will not longer hold that
      value. You'll need to use a reference (&) to point to the resource"
   */

   //How not to do it:
   // let vec1 = vec![1,2,3];
   // let vec2 = vec1;

   //   println!("\nValues: {:?}", (vec1, vec2));

   //We have to make it a reference to the original vector using the ampersand
   let vec1 = vec![1,2,3];
   let vec2 = &vec1;

   //Ampersand again for the original
   println!("\nValues: {:?}", (&vec1, vec2));



}
