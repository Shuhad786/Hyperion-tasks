
public class Person {
	
	// attributes
	int number;
	String name;
	String emailAddress;
	String addressName;
	String assignedProject;
	int contactNumber;
	
	
	public Person(int number, String name, String emailAddress, String addressName, String assignedProject, int contactNumber) {
		
		// objects
		this.number = number;
		this.name = name;
		this.emailAddress = emailAddress;
		this.addressName = addressName;
		this.assignedProject = assignedProject;
		this.contactNumber = contactNumber;
	}
	
	// methods
	public int collectconNum() {
		return number;
	}
	
	public String collectconName() {
		return name;
	}
		
	public String collectemail() {
		return emailAddress;
	}
	
	public String collectAddressName() {
		return addressName;
	}
	
	public String collectAssign() {
		return assignedProject;
	}
	
	public int contactNumber() {
		return contactNumber;
	}
	
	public void newContact(int contactNumber) {
		this.contactNumber = contactNumber;
	}
	
	public void newEmail(String emailAddress) {
		this.emailAddress = emailAddress;
	}
	
	// to string method
	public String toString() {
		String output = "The contact number of the person is: \n" + number + "\n";
		output += "The persons name is: \n" + name + "\n";
		output += "The email address of the person is : \n" + emailAddress + "\n";
		output += "The name of the address is: \n" + addressName + "\n";
		output += "The project is assigned to: \n" + assignedProject;
		
		return output;
	}

}



