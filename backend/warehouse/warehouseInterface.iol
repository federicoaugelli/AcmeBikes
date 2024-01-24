type Component: void {
     .componentId: int
     .orderId: int
}

type ComponentRequest: void{
    .components[0, *]: Component
}

type ComponentId: void {
     .component_id: int
}

type Test: void {
     .test: string
}

interface warehouseInterface {
     RequestResponse: getStatus(Test)(Test)
}

interface AcmeDbInterface {
    RequestResponse: checkIsAssembleable(ComponentId)(int)
}