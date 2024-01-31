include "console.iol"
include "warehouseInterface.iol"

inputPort MainWarehouseService {
	Location: "socket://localhost:8085"
	Protocol: soap
	Interfaces: warehouseInterface
}

interface CourierInterface {
    RequestResponse: shipment(ComponentRequest)(string)
}


interface SupplierInterface {
    RequestResponse: getComponent(ComponentRequest)(string)
}

outputPort CourierService {
    Location: "socket://localhost:8001/"
    Protocol: http { .method = "post" }
    Interfaces: CourierInterface
}

outputPort SupplierService {
    Location: "socket://localhost:8003/"
    Protocol: http { .method = "get" }
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
		componentsForSupplier[0] = void
		componentsForCourier[0] = void
		componentsForAcmeBike[0] = void
		for (component in ComponentRequest.components) {
			if (component.qty < 0){
				componentsForSupplier[ #componentsForSupplier ] = component
			}
		}
		// Chiedere al fornitore esterno
		getComponent@SupplierService(componentsForSupplier)( supplierResponse );
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