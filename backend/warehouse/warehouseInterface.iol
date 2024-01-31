type ComponentRequest: void{
    .components[0, *]: Component
}

type ComponentResponse: void{
    .components[0, *]: Component
}

type Component: void {
     .component_id: int
     .qty: int
     .assembleable: bool
}

type Test: void {
     .test: string
}

interface warehouseInterface {
     RequestResponse: getStatus(Test)(Test)
     RequestResponse: checkComponents(ComponentRequest)(ComponentResponse)
}

interface AcmeDbInterface {
    RequestResponse: checkIsAssembleable(ComponentRequest)(int)
}