<script>
    import { firebaseConfig } from "$lib/firebase";
    import { initializeApp } from "firebase/app";
    import { getFirestore, collection, getDocs, query, where } from "firebase/firestore";

    import Icon from 'svelte-awesome';
    import { calendar } from 'svelte-awesome/icons';

    const fb = initializeApp(firebaseConfig);
    const db = getFirestore(fb);

    async function newEventList() {
        const q = query(collection(db, "Events"), where("Date",">=",new Date()))
        const eventQuery = await getDocs(q);
        return eventQuery.docs;
    }

    async function oldEventList() {
        const q = query(collection(db, "Events"), where("Date","<=",new Date()))
        const eventQuery = await getDocs(q);
        return eventQuery.docs;
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
            {#each evs as ev}
                <tr class="eventrow">
                <td>{ev.data().Title}</td>
                <td>{ev.data().Date.toDate()}</td>
                <td>{ev.data().Location}</td>
                <td>{ev.data().Description}</td>
                <td class="text-center"><a href="/event/{ev.id}" class="text-primary"><Icon data={calendar} /></a></td>
                </tr>
            {/each}
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
            {#if evs.length > 0}
                {#each evs as ev}
                    <tr class="eventrow">
                    <td>{ev.data().Title}</td>
                    <td>{ev.data().Date.toDate()}</td>
                    <td>{ev.data().Location}</td>
                    <td>{ev.data().Description}</td>
                    <td></td>
                    </tr>
                {/each}
            {:else}
                    <tr><td colspan="5" class="text-center">No past events yet...</td></tr>
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