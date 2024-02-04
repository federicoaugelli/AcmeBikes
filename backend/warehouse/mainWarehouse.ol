include "console.iol"
include "warehouseInterface.iol"
include "json_utils.iol"

inputPort MainWarehouseService {
	Location: "socket://localhost:8085"
	Protocol: soap
	Interfaces: warehouseInterface
}

interface CourierInterface {
    RequestResponse: shipment(ComponentRequest)(string)
}


interface SupplierInterface {
    RequestResponse: supplier(ComponentRequest)(string)
}

outputPort CourierService {
    Location: "socket://localhost:8001/"
    Protocol: http { .method = "post" }
    Interfaces: CourierInterface
}

outputPort SupplierService {
    Location: "socket://localhost:8003/"
    Protocol: http { .method = "post" }
    Interfaces: SupplierInterface
}

execution{ concurrent }

main{

	[getStatus(request)(response){
		response.test = "OK"

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
		getJsonString@JsonUtils( componentsForSupplier )( componentsForSupplierJson );
		println@Console( componentsForSupplierJson )()
		supplier@SupplierService(componentsForSupplier)( supplierResponse );
    	println@Console( supplierResponse )()

		
		for (component in componentsRequest.components) {
			if (component.assembleable){
				componentsForCourier[ #componentsForCourier ]  = component
			}
			else {
				componentsForAcmeBike[ #componentsForAcmeBike ] = component
			}
		}
		// Contattare corriere
		shipment@CourierService(componentsForCourier)( courierResponse );
    	println@Console( courierResponse )()

		response.components = componentsForAcmeBike
	}]{
		println@Console( response )()
	}
}