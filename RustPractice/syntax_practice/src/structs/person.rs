pub struct Person{
   pub first_name : String,
   pub last_name: String
}

impl Person{
   pub fn new(first: &str, last: &str) -> Person{
      Person{
         first_name : first.to_string(),
         last_name : last.to_string(),
      }
   }

   //setters and getters
   pub fn set_first_name(&mut self, new_first: &str){self.first_name = new_first.to_string();}

   pub fn set_last_name(&mut self, new_last: &str){self.last_name = new_last.to_string();}

   pub fn get_first_name(&self) -> String{format!("{}",self.first_name)}

   pub fn get_last_name(&self) -> String{format!("{}",self.last_name)}

   //helper functions

   pub fn get_full_name(&self) -> String{format!("{} {}", self.first_name, self.last_name)}

   pub fn to_tuple(self) -> (String, String) {(self.first_name, self.last_name)}

}