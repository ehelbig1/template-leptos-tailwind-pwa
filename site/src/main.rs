use leptos::*;
use tracing_subscriber::fmt;
use tracing_subscriber_wasm::MakeConsoleWriter;

fn main() {
    fmt()
    .with_writer(
        MakeConsoleWriter::default()
            .map_trace_level_to(tracing::Level::INFO),
    )
    .without_time()
    .init();

    console_error_panic_hook::set_once();

    tracing::info!("starting!");

    mount_to_body(|| view! { <App/> })
}

#[component]
fn App() -> impl IntoView {
    let (count, set_count) = create_signal(0);

    view! {
        <div class="w-full h-full bg-blue-500 grid grid-cols-2 gap-4 place-items-center">
            <button
                class="size-2xl"
                on:click=move |_| {set_count(count() + 1)}
            >       
                "Click me:" {count}
            </button>
            <p class="bg-green-100">"Hello"</p>
            <p>"Hello"</p>
            <p>"Hello"</p>
            <p>"Hello"</p>
            <p>"Hello"</p>
            <p>"Hello"</p>
        </div>
    }
}