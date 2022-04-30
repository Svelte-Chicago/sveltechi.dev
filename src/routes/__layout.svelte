<script>
    import "../app.css";
</script>

<svelte:head>
    <title>Svelte Society - Chicago</title>
    <link rel="icon" href="/svelte_chicago_125x125.png" />
</svelte:head>
<div class="fixed top-0 right-0 rounded-l-full  text-xl flex flex-row justify-end align-baseline bg-red-600 z-10 text-white">
    <div class="pl-8" />
    <div class="p-2">
        <a href="/events">Events</a>
    </div>
    <div class="p-2">
        <a href="/">Home</a>
    </div>
    <div class="pr-8" />
</div>
<div class="flex flex-col items-center max-h-screen">
    <slot />
</div>

