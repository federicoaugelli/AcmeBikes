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