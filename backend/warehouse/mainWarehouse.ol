include "console.iol"
include "warehouseInterface.iol"
include "http.iol"

inputPort MainWarehouseService {
	Location: "socket://localhost:8005"
	Protocol: sodep
	Interfaces: warehouseInterface
}

outputPort AcmeDbService {
    Location: "socket://localhost:8004/"
    Protocol: http { .method = "get" }
    Interfaces: AcmeDbInterface
}

cset {
}

execution{ concurrent }

init {
}

main{

    while(true){
    	[sendComponent(ComponentRequest)(response){
            foreach (component : ComponentRequest){
				request.component_id = component.componentId
                checkIsAssembleable@SumService(request)( response );
				println@Console("Response:" + response)()
			}
    	}]{
    		println@Console("")()
    	}
    }

}