import java.util.Scanner;

public class PoisedDataCollector {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Please enter the number of the project: ");
		int number = input.nextInt();
		
		System.out.print("Please enter the name of the project: ");
		String name = input.next();
		
		System.out.print("Please enter the type of building being designed: ");
		String buildingType = input.next();
		
		System.out.print("please enter the address name of the project: ");
		String addressName = input.next();
		
		System.out.print("please enter the address number of the project: ");
		int addressNumber = input.nextInt();
		
		System.out.print("Please enter the erf number: ");
		int erfNumber = input.nextInt();
		
		System.out.print("Please enter the total fee of the project: ");
		int totalFee = input.nextInt();
		
		System.out.print("Please enter the total paid to the current date: ");
		int totalPaid = input.nextInt();
		
		System.out.print("Please enter the dead line of the project: ");
		String deadLine = input.next();
		
		System.out.print("Please enter the architects ID number: "); // unique number of the architect on database
		int architectID = input.nextInt();
		
		System.out.print("Please enter the customers ID number: "); // unique number of the customer on database
		int customerID = input.nextInt();
		
		System.out.print("Please enter the contractors ID number: "); // unique number of the contractor database
		int contractorID = input.nextInt();
		
		Project data = new Project(number, name, buildingType, addressName, addressNumber, erfNumber, architectID, customerID, contractorID, totalFee, totalPaid, deadLine);
		
		System.out.println("Project data: \n" + data.toString());
		
		System.out.print("Is the project completed?, Yes or No: ");
		String complete = input.next();
		if (complete == "Yes") {
				System.out.print("Is the total fee paid in full?, Yes or No: ");
				String total = input.next();
				if (total == "Yes") {
					System.out.println("Project can now be finalised");
				}
				else {
					int remainder = totalFee - totalPaid;
					System.out.println("The outstanding amount to be paid is: R" + remainder);
				}
		
		}
		else {
			System.out.print("Please enter the new dead line: ");
			data.setDeadLine(input.next());
		}
		
		System.out.print("Please enter the number of the person: ");
		int number1 = input.nextInt();
		
		System.out.print("Please enter the name of the person: ");
		String name1 = input.next();
		
		System.out.print("Please enter the email address of the person: ");
		String emailAddress = input.next();
		
		System.out.print("Please enter the address of the person: ");
		String addressName1 = input.next();
		
		System.out.print("Please enter the name of the person the project is assigned to: ");
		String assignedProject = input.next();
		
		System.out.print("Please enter the name of the person the project is assigned to: ");
		int contactNumber1 = input.nextInt();
		
		Person info = new Person(number1, name1, emailAddress, addressName1, assignedProject, contactNumber1);
		
		System.out.print("Person information is: " + info.toString());
		
		System.out.print("Would you like to change the contractors details?, Yes or No: ");
		String foreman = input.next();
		if (foreman == "Yes") {
			System.out.print("Please enter new contact details: ");
			info.newContact(input.nextInt());
			System.out.print("Please enter new email address: ");
			info.newEmail(input.next());
		}
	
	
	}
}
