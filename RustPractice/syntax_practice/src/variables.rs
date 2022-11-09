pub fn run(){

    //immutable variable
    let string_variable = "Jason";

    //mutable variable
    let mut mutable_variable = "Richard";

    // constants (upper case for constants)
    const ID: i32 = 1345678;

    // multiple variables can be defined on one line

    let (roof_material, roof_height) = ("Asphalt Shingle", 15);


    // mutable variables are similar in definition
    let (savings_account_name, mut savings_account_balance, mut credit_card_balance) = ("Chequing", 1243, 230);

    //String variables
    println!("My name is {}", string_variable);
    println!("I can also say my name is {string_variable} like this!\n");

    //Immutable Variables
    print!("My name used to be {}", mutable_variable);
    mutable_variable = "Dick";
    println!(", but then I changed it to {}", mutable_variable);
    println!("Though my name has changed, but government ID is still {}.\n", ID);

    println!("My old roof was made of {} and was only {}ft off the ground!\n", roof_material, roof_height);

    // Mutable Variables
    print!("Current {} account balance of ${}, less the credit card balance of ${} equals $", savings_account_name, savings_account_balance, credit_card_balance);
    savings_account_balance -= credit_card_balance;
    credit_card_balance = 0;
    println!("{}\n",savings_account_balance);

}