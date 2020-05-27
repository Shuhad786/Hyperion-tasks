
public class Project {
	
	// attributes
	int number; // the number of the project links with the number in 'Person class'
	String name; // name of the project
	String buildingType; 
	String addressName; // physical address of the project
	int addressNumber; // the number of the physical address
	int erfNumber;
	int totalFee; // total amount of the project
	int totalPaid; // the total paid to date 
	String deadLine; // the time the project must be completed by
	int architectID; // unique number given to the architect as reference to the project
	int customerID; // unique number given to the customer as reference to the project
	int contractorID; // unique number given to the contractor as reference to the project
	
	public Project(int number, String name, String buildingType, String addressName, int addressNumber, int erfNumber, int architectID, int customerID, int contractorID, int totalFee, int totalPaid, String deadLine) {
		
		// objects
		this.number = number;
		this.name = name;
		this.buildingType = buildingType;
		this.addressName = addressName;
		this.addressNumber = addressNumber;
		this.erfNumber = erfNumber;
		this.architectID = architectID;
		this.customerID = customerID;
		this.contractorID = contractorID;
		this.totalFee = totalFee;
		this.totalPaid = totalPaid;
		this.deadLine = deadLine;
	}
	// methods
	
	public int collectPrjtNum() {
		return number;
	}
	
	public String collectPrjtName() {
		return name;
	}
		
	public String collectBuildType() {
		return buildingType;
	}
	
	public String collectAddressName() {
		return addressName;
	}
	
	public int collectAddressNum() {
		return addressNumber;
	}
	
	public int collectErfNum() {
		return erfNumber;	
	}
	
	public int collectArchID() {
		return architectID;	
	}
	
	public int collectCustID() {
		return customerID;	
	}
	
	public int collectConID() {
		return contractorID;	
	}
	
	public int collectTotFee() {
		return totalFee;	
	}
	
	public int collectTotPaid() {
		return totalPaid;	
	}
	
	public String collectDeadLine() {
		return deadLine;	
	}
	
	public void setDeadLine(String deadLine) {
		this.deadLine = deadLine;	
	}


	// to string method
	public String toString() {
		String output = "The project number is: \n" + number + "\n";
		output += "The project name is: \n" + name + "\n";
		output += "The type of building is a: \n" + buildingType + "\n" ;
		output += "The name of the address is: \n" + addressName + "\n";
		output += "The number of the address is: \n" + addressNumber + "\n";
		output += "The erf number is: \n" + erfNumber + "\n";
		output += "The architects ID is: \n" + architectID + "\n";
		output += "The customers ID is: \n" + customerID + "\n";
		output += "The contractors ID is: \n" + contractorID + "\n";
		output += "The total fee is: R \n" + totalFee + "\n";
		output += "The total paid to date is: R \n" + totalPaid + "\n";
		output += "The dead line is: \n" + deadLine;
		
		return output;
	}

}
