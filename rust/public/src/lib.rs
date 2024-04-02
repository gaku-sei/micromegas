//! micromegas : scalable telemetry

pub use object_store;

pub mod telemetry {
    pub use micromegas_telemetry::*;
}

pub mod ingestion {
    pub use micromegas_ingestion::*;
}
