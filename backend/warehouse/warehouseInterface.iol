type ComponentRequest: void{
    .resale_instance_id: string
    .components[0, *]: Component
}

type ComponentCourierRequest: void{
    .resale_instance_id: string
    .components[0, *]: Component
    .contact_resale: bool
}

type BikeRequest: void{
    .bikes[0, *]: Bike
}

type BikeResponse: void{
    .bikes[0, *]: Bike
}

type Bike: void{
    .bike_id: int
    .qty: int
}

type ComponentSupplierRequest: void{
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

interface WarehouseInterface {
     RequestResponse: checkBikes(BikeRequest)(BikeResponse)
     RequestResponse: checkComponents(ComponentRequest)(ComponentResponse)
}

interface AcmeDbInterface {
    RequestResponse: checkIsAssembleable(ComponentRequest)(int)
}