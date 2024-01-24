include "console.iol"
include "warehouseInterface.iol"

inputPort MainWarehouseService {
	Location: "socket://localhost:8085"
	Protocol: soap
	Interfaces: warehouseInterface
}

outputPort AcmeDbService {
    Location: "socket://localhost:8004/"
    Protocol: http { .method = "get" }
    Interfaces: AcmeDbInterface
}

execution{ concurrent }

main{

	[getStatus(request)(response){
		response.test = "OK"

	}]{
		println@Console( response )()
	}


}