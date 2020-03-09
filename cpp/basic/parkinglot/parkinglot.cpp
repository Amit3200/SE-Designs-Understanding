//author : 'Amit Singh Sansoya @amit3200'
//it was all meant to happen as i was all talk!
#include<bits/stdc++.h>
using namespace std;
class Vehicle{
	private:
		int size;
		string vehicleNum;
		string vehicleName;
	public:
		Vehicle(){}
		
		string getVehicleName(){
			return vehicleName;
		}
		
		string getVehicleNum(){
			return vehicleNum;
		}
		
		int getVehicleSize(){
			return size;
		}
		
		void setVehicleName(string vehicleName){
			this->vehicleName=vehicleName;
		}
		
		void setVehicleNum(string vehicleNum){
			this->vehicleNum=vehicleNum;
		}
		
		void setSize(int size){
			this->size=size;
		}
		
		virtual void provideDetails(string name,string no){}
};

class Car:public Vehicle{
	public:
		Car(){
			setSize(3);								
		}
		
		virtual void provideDetails(string carName,string carNumber){
			setVehicleName(carName);
			setVehicleNum(carNumber);
		
		}
};

class ParkingLot{
	private:
		unordered_map<int,vector<bool>> parkingBuilding;
		unordered_map<bool,int> spotAvailability;
		map<pair<int,int>,Vehicle*> slotVehicle;
		map<Vehicle*,pair<int,int>> vehicleMarker;
	public:
		ParkingLot(){
			for(int i=1;i<=5;i++){
				vector<bool> vacant(20,true);
				parkingBuilding[i]=vacant;
			}
			spotAvailability[true]=20*5;
			spotAvailability[false]=0;
		}
		void placeVehicleInSlot(Vehicle *vehicle);
		void removeVehicleFromSlot(Vehicle *vehicle);
		void locateParkedVehicle(Vehicle *vehicle);
		void getParkingCurrentStatus();
		pair<int,int> getVacantSpace();
		bool isSpotAvaibileInLot();
		virtual ~ParkingLot(){}
};

class ParkingSlot:public ParkingLot{
	private:
		pair<int,int> slotId;
	public:
		static int ticketNums;
		ParkingSlot(){}
		ParkingSlot(pair<int,int> slotId){
			this->slotId=slotId;
		}
		pair<int,int> getSlotId(){
			return slotId;
		}
		pair<int,int> assignVehicleParkingLocation(Vehicle *vehicle);
		void releaseVehcileFromParkingLocation();
		virtual ~ParkingSlot(){}
};

bool ParkingLot::isSpotAvaibileInLot(){
	if(spotAvailability[true]>0)
		return true;
	return false;
}

pair<int,int> ParkingLot::getVacantSpace(){
	for(int i=1;i<=5;i++){
		for(int j=0;j<20;j++){
			if(parkingBuilding[i][j]==true){
				return {i,j};		
			}
		}
	}
	return {-1,-1};
}

pair<int,int> ParkingSlot::assignVehicleParkingLocation(Vehicle *vehicle){
	pair<int,int> assignedCoordinates=getSlotId();
	return assignedCoordinates;
}

void ParkingLot::placeVehicleInSlot(Vehicle *vehicle){
	pair<int,int> getVacantCoordinates=this->getVacantSpace();
	if(getVacantCoordinates.first==-1 && getVacantCoordinates.second==-1){
		throw "Space Not Found";	
	}
	else{
		ParkingSlot pSlot({getVacantCoordinates.first,getVacantCoordinates.second});
		pair<int,int> assignedCoordinates=pSlot.assignVehicleParkingLocation(vehicle);
		parkingBuilding[assignedCoordinates.first][assignedCoordinates.second]=false;
		if(slotVehicle.find(assignedCoordinates)==slotVehicle.end())
			slotVehicle[assignedCoordinates]=vehicle;
		else
			throw "Already Occupied, Trying to push on same place";
		if(vehicleMarker.find(vehicle)==vehicleMarker.end())
			vehicleMarker[vehicle]=assignedCoordinates;
		else
			throw "Vehicle Found at the Slot";
		this->spotAvailability[true]-=1;
		this->spotAvailability[false]+=1;
	}
}
void ParkingLot::locateParkedVehicle(Vehicle *vehicle){
	if(vehicleMarker.find(vehicle)==vehicleMarker.end()){
		cout<<"No Vehicle Found\n";
	}
	else{
		cout<<"Vehicle Found\n";
		cout<<vehicle->getVehicleNum()<<"\n";
		cout<<vehicle->getVehicleName()<<"\n";
		cout<<vehicleMarker[vehicle].first<<" "<<vehicleMarker[vehicle].second<<"\n";
	}
}

void ParkingLot::getParkingCurrentStatus(){
	cout<<"--------------------------------------------------------------\n";
	cout<<"Vacant -> "<<spotAvailability[true]<<"\n";
	cout<<"Filled -> "<<spotAvailability[false]<<"\n";
	cout<<"Floor Wise View\n";
	for(int i=1;i<=5;i++){
		int vacants=0,occupied=0;
		for(int j=0;j<20;j++){
			if(parkingBuilding[i][j])
				vacants++;
			else
				occupied++;
		}
		cout<<"Floor "<<i<<" - Vacants - "<<vacants<<" "<<" - occupied - "<<occupied<<"\n";
	}
	cout<<"--------------------------------------------------------------\n";
}

int main(){
	ParkingLot abcParking;
	Vehicle *car1=new Car;
	car1->provideDetails("abcd","WB 24 R 2310");
	if(abcParking.isSpotAvaibileInLot()){
		abcParking.placeVehicleInSlot(car1);
		abcParking.locateParkedVehicle(car1);
		abcParking.getParkingCurrentStatus();
	}
	Vehicle *car2=new Car;
	car2->provideDetails("alto","WB 25 R 1110");
	Vehicle *car3=new Car;
	car3->provideDetails("sx4","WB 26 K 2220");
	Vehicle *car4=new Car;
	car4->provideDetails("nexon","WB 27 W 3330");
	Vehicle *car5=new Car;
	car5->provideDetails("harrier","WB 28 Q 4410");
	abcParking.placeVehicleInSlot(car2);
	abcParking.locateParkedVehicle(car2);
	abcParking.placeVehicleInSlot(car3);
	abcParking.locateParkedVehicle(car3);
	abcParking.placeVehicleInSlot(car4);
	abcParking.locateParkedVehicle(car4);
	abcParking.placeVehicleInSlot(car5);
	abcParking.locateParkedVehicle(car5);
	abcParking.getParkingCurrentStatus();
	Vehicle *car6=new Car;
	car6->provideDetails("hexa","WB 29 S 5130");
	Vehicle *car7=new Car;
	car7->provideDetails("nios","WB 34 Z 3130");
	Vehicle *car8=new Car;
	car8->provideDetails("i10","WB 35 X 5140");
	Vehicle *car9=new Car;
	car9->provideDetails("elantra","WB 36 C 1230");
	Vehicle *car10=new Car;
	car10->provideDetails("compass","WB 36 T 2130");
	abcParking.placeVehicleInSlot(car6);
	abcParking.locateParkedVehicle(car6);
	abcParking.placeVehicleInSlot(car7);
	abcParking.locateParkedVehicle(car7);
	abcParking.placeVehicleInSlot(car8);
	abcParking.locateParkedVehicle(car8);
	abcParking.placeVehicleInSlot(car9);
	abcParking.locateParkedVehicle(car9);
	abcParking.placeVehicleInSlot(car10);
	abcParking.locateParkedVehicle(car10);
	abcParking.getParkingCurrentStatus();
}

