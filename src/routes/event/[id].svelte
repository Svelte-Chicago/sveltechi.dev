<script>
    import { page } from '$app/stores';

    const id = $page.params.id;

    async function getEvent(id) {

        const response =  await fetch(`/api/event/${id}`);
        const data = await response.json();
        return data;
    }

    function date_format(timestamp) {
        return new Date(timestamp*1000)
    }

</script>

{#await getEvent(id)}
    Loading Event...
{:then ev}
    <div class="relative top-12 max-w-3xl flex flex-col justify-center">
        <div class="">
            <div class="text-xl">Event: {ev.Title}</div>
            <div>When: {date_format(ev.Date)} </div>
            <div>Where: {ev.Location}</div>
            <div>What: {ev.Description}</div>
        </div>
        <div class="pt-12">
            We're just getting started! Sign-ups will be open soon
        </div>
    </div>
{/await}