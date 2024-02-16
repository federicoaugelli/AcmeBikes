include "console.iol"
include "warehouseInterface.iol"
include "json_utils.iol"

inputPort SecondaryWarehouseService {
	Location: "socket://localhost:8086"
	Protocol: soap
	Interfaces: WarehouseInterface
}

interface CourierInterface {
    RequestResponse: shipment(ComponentCourierRequest)(string)
}


interface SupplierInterface {
    RequestResponse: supplyComponents(ComponentSupplierRequest)(string)
    RequestResponse: supplyBikes(BikeRequest)(string)
}

interface AcmeDBInterface {
    RequestResponse: component(ModifyComponent)(string)
    RequestResponse: bike(ModifyBike)(string)
}

outputPort CourierService {
    Location: "socket://localhost:8001/"
    Protocol: http { 
		.method = "post"
		.format = "json" }
    Interfaces: CourierInterface
}

outputPort SupplierService {
    Location: "socket://localhost:8003/"
    Protocol: http { 
		.method = "post"
		.format = "json" }
    Interfaces: SupplierInterface
}

outputPort AcmeDBService {
    Location: "socket://localhost:8004/"
    Protocol: http { 
		.method = "put"
		.format = "json" }
    Interfaces: AcmeDBInterface
}

execution{ concurrent }

main{

	[checkBikes(bikeRequest)(response){
		i = 0
		for (bike in bikeRequest.bikes) {
			if (bike.qty < 0){
				bikeForSupplier.bikes[i] << bike
				i = i + 1
			}
		}
		supplyBikes@SupplierService(bikeForSupplier)( supplierResponse );
    	println@Console( supplierResponse )()

		for (bike in bikeForSupplier.bikes) {
			request.bike_id = bike.bike_id
			request.qty = bike.qty * -1
			bike@AcmeDBService(request)( dbResponse );
    		println@Console( dbResponse )()
		}

		response = bikeRequest
	}]{
		println@Console( response )()
	}
	[checkComponents(componentsRequest)(response){
		i = 0
		for (component in componentsRequest.components) {
			if (component.qty < 0){
				componentsForSupplier.components[i] << component
				i = i + 1
			}
		}
		// Chiedere al fornitore esterno
		supplyComponents@SupplierService(componentsForSupplier)( supplierResponse );
    	println@Console( supplierResponse )()

		for (component in componentsForSupplier.components) {
			request.prod_id = component.component_id
			request.qty = component.qty * -1
			component@AcmeDBService(request)( dbResponse );
    		println@Console( dbResponse )()
		}

		j = 0
		z = 0
		for (component in componentsRequest.components) {
			if (component.assembleable){
				componentsForCourier.components[j] << component
				j = j + 1
			}
			else {
				componentsForAcmeBike.components[z] << component
				z = z + 1
			}
		}
		componentsForCourier.resale_instance_id = componentsRequest.resale_instance_id
		componentsForCourier.contact_resale = false
		// Contattare corriere
		if (j > 0) {
			shipment@CourierService(componentsForCourier)( courierResponse );
			println@Console( courierResponse )()
		}

		response = componentsForAcmeBike
	}]{
		println@Console( response )()
	}
}