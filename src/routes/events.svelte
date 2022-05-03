<script>
    import Icon from 'svelte-awesome';
    import { calendar } from 'svelte-awesome/icons';

    const newEventList = (async () => {
        const response =  await fetch('/api/events');
        const data = await response.json();
        return data;
    })

    const oldEventList = (async () => {
        const response =  await fetch('/api/events?old=true');
        const data = await response.json();
        return data;
    })

    function date_format(timestamp) {
        console.log(timestamp*1000)
        return new Date(timestamp*1000)
    }


</script>

<div class="relative top-[3rem] max-w-3xl">
    <div class="text-center font-bold text-2xl">Upcoming Events</div>
    <table>
        <thead class="font-bold">
            <td>What?</td><td>Date & Time</td><td>Location</td><td>Description</td><td>Join Us</td>
        </thead>

        {#await newEventList()}
            <tr>
                <td colspn="5">Getting upcoming events...</td>
            </tr>

        {:then evs}
            {#if evs.events.length > 0}
                {#each evs.events as ev}
                    <tr class="eventrow">
                    <td>{ev.Title}</td>
                    <td>{date_format(ev.Date)}</td>
                    <td>{ev.Location}</td>
                    <td>{ev.Description}</td>
                    <td class="text-center"><a href="/event/{ev.id}" class="text-primary"><Icon data={calendar} /></a></td>
                    </tr>
                {/each}
            {:else}
                <tr><td colspan="5" class="text-center">No upcoming events currently scheduled</td></tr>
            {/if}
        {:catch error}
            <tr><td>Could not get events...</td></tr>
        {/await}

    <tr><td colspan="5">&nbsp;</td></tr>
    <tr><td colspan="5">&nbsp;</td></tr>
        <thead class="font-bold">
            <tr>
                <td colspan="5" class="text-center font-bold text-2xl">Past Events</td>
            </tr>
            <td>What?</td><td>Date & Time</td><td>Location</td><td>Description</td><td></td>
        </thead>
        {#await oldEventList()}
            <tr>
                <td colspn="5">Getting past events...</td>
            </tr>

        {:then evs}
            {#if evs.events.length > 0}
                {#each evs.events as ev}
                    <tr class="eventrow">
                        <td>{ev.Title}</td>
                        <td>{date_format(ev.Date)}</td>
                        <td>{ev.Location}</td>
                        <td>{ev.Description}</td>
                    <td></td>
                    </tr>
                {/each}
            {:else}
                    <tr><td colspan="5" class="text-center">No past events yet</td></tr>
            {/if}
        {:catch error}
            <tr><td>Could not get events...</td></tr>
        {/await}

    </table>
</div>

<style>
    td {
        padding: 0 1rem;
    }

    tr.eventrow:nth-child(odd) {
        background-color:#b3ddf2;
    }
</style>